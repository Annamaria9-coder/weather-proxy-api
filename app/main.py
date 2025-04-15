"""Main module for the Weather Proxy API.

This module defines the FastAPI application and endpoints.
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
from typing import Optional, Dict, Any

from app.weather import get_weather_data
from app.cache import get_cache_stats, clear_cache

# Create FastAPI application
app = FastAPI(
    title="Weather Proxy API",
    description="A proxy API for OpenWeatherMap with caching and custom messages",
    version="1.0.0"
)


@app.get("/")
async def root():
    """Root endpoint that returns API information."""
    return {
        "name": "Weather Proxy API",
        "version": "1.0.0",
        "description": "A proxy API for OpenWeatherMap with caching and custom messages",
        "endpoints": [
            "/weather/{city}",
            "/cache/stats",
            "/cache/clear"
        ]
    }


@app.get("/weather/{city}")
async def get_weather(city: str, use_cache: bool = Query(True, description="Whether to use cached data if available")):
    """Get weather data for a specified city.
    
    Args:
        city (str): Name of the city to get weather data for
        use_cache (bool): Whether to use cached data if available
    """
    try:
        weather_data = await get_weather_data(city, use_cache)
        return weather_data
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        if "not found" in str(e).lower():
            raise HTTPException(status_code=404, detail=f"City '{city}' not found")
        raise HTTPException(status_code=500, detail=f"Error fetching weather data: {str(e)}")


@app.get("/cache/stats")
async def cache_stats():
    """Get statistics about the current cache state."""
    return get_cache_stats()


@app.delete("/cache/clear")
async def cache_clear():
    """Clear all entries from the cache."""
    clear_cache()
    return {"message": "Cache cleared successfully"}


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Custom exception handler for HTTP exceptions."""
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail}
    )


@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    """Custom exception handler for general exceptions."""
    return JSONResponse(
        status_code=500,
        content={"error": f"An unexpected error occurred: {str(exc)}"}
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)