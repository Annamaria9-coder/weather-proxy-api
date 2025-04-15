"""Weather module for the Weather Proxy API.

This module handles interactions with the OpenWeatherMap API
and processes the weather data.
"""

import httpx
from typing import Dict, Any, Optional

from app.config import OPENWEATHER_API_KEY, OPENWEATHER_BASE_URL
from app.cache import get_from_cache, add_to_cache
from app.utils import kelvin_to_celsius, get_weather_message


async def get_weather_data(city: str, use_cache: bool = True) -> Dict[str, Any]:
    """Get weather data for a specified city.
    
    Args:
        city (str): Name of the city to get weather data for
        use_cache (bool): Whether to use cached data if available
        
    Returns:
        Dict[str, Any]: Processed weather data with custom message
        
    Raises:
        HTTPStatusError: If the API request fails
        ValueError: If the API key is not configured
    """
    if not OPENWEATHER_API_KEY:
        raise ValueError("OpenWeatherMap API key is not configured")
    
    # Check cache first if enabled
    if use_cache:
        cached_data = get_from_cache(city)
        if cached_data:
            return cached_data
    
    # Prepare API request parameters
    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
    }
    
    # Make API request
    async with httpx.AsyncClient() as client:
        response = await client.get(OPENWEATHER_BASE_URL, params=params)
        response.raise_for_status()  # Raise exception for HTTP errors
        
        data = response.json()
    
    # Process the weather data
    processed_data = process_weather_data(data)
    
    # Cache the processed data
    if use_cache:
        add_to_cache(city, processed_data)
    
    return processed_data


def process_weather_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """Process raw weather data from OpenWeatherMap API.
    
    Args:
        data (Dict[str, Any]): Raw weather data from OpenWeatherMap API
        
    Returns:
        Dict[str, Any]: Processed weather data with additional information
    """
    # Extract relevant information
    main_data = data.get("main", {})
    weather_info = data.get("weather", [{}])[0]
    
    # Convert temperatures
    temp_kelvin = main_data.get("temp")
    temp_celsius = kelvin_to_celsius(temp_kelvin) if temp_kelvin else None
    
    # Get weather condition
    weather_condition = weather_info.get("description", "")
    
    # Generate custom message
    custom_message = get_weather_message(temp_celsius, weather_condition) if temp_celsius else ""
    
    # Create processed data dictionary
    processed_data = {
        "city": data.get("name"),
        "country": data.get("sys", {}).get("country"),
        "temperature": {
            "kelvin": temp_kelvin,
            "celsius": round(temp_celsius, 1) if temp_celsius else None,
            "fahrenheit": round(kelvin_to_celsius(temp_kelvin) * 9/5 + 32, 1) if temp_kelvin else None
        },
        "weather": {
            "main": weather_info.get("main"),
            "description": weather_condition,
            "icon": weather_info.get("icon")
        },
        "details": {
            "humidity": main_data.get("humidity"),
            "pressure": main_data.get("pressure"),
            "wind_speed": data.get("wind", {}).get("speed"),
            "clouds": data.get("clouds", {}).get("all")
        },
        "custom_message": custom_message
    }
    
    return processed_data