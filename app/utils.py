"""Utility functions for the Weather Proxy API.

This module provides helper functions for formatting weather data
and generating custom messages based on weather conditions.
"""

def kelvin_to_celsius(kelvin):
    """Convert temperature from Kelvin to Celsius.
    
    Args:
        kelvin (float): Temperature in Kelvin
        
    Returns:
        float: Temperature in Celsius
    """
    return kelvin - 273.15


def kelvin_to_fahrenheit(kelvin):
    """Convert temperature from Kelvin to Fahrenheit.
    
    Args:
        kelvin (float): Temperature in Kelvin
        
    Returns:
        float: Temperature in Fahrenheit
    """
    celsius = kelvin_to_celsius(kelvin)
    return (celsius * 9/5) + 32


def get_weather_message(temp_celsius, weather_condition):
    """Generate a custom message based on temperature and weather condition.
    
    Args:
        temp_celsius (float): Temperature in Celsius
        weather_condition (str): Weather condition description
        
    Returns:
        str: Custom weather message
    """
    # Temperature-based messages
    if temp_celsius > 30:
        temp_message = "It's very hot! Stay hydrated."
    elif temp_celsius > 20:
        temp_message = "It's warm and pleasant."
    elif temp_celsius > 10:
        temp_message = "It's cool outside."
    elif temp_celsius > 0:
        temp_message = "It's cold, consider wearing a jacket."
    else:
        temp_message = "It's freezing! Bundle up well."
    
    # Weather condition-based messages
    condition_lower = weather_condition.lower()
    if "rain" in condition_lower or "drizzle" in condition_lower:
        condition_message = "Don't forget your umbrella!"
    elif "snow" in condition_lower:
        condition_message = "Watch out for snow and ice!"
    elif "cloud" in condition_lower:
        condition_message = "It's cloudy today."
    elif "clear" in condition_lower:
        condition_message = "Clear skies ahead!"
    elif "fog" in condition_lower or "mist" in condition_lower:
        condition_message = "Be careful of reduced visibility."
    elif "thunder" in condition_lower or "storm" in condition_lower:
        condition_message = "Stormy weather! Stay safe indoors if possible."
    else:
        condition_message = ""
    
    # Combine messages
    if condition_message:
        return f"{temp_message} {condition_message}"
    else:
        return temp_message