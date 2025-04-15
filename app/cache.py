"""Cache module for the Weather Proxy API.

This module provides a simple in-memory cache implementation
to store weather data and reduce the number of API calls.
"""

import time
from typing import Dict, Any, Tuple
from app.config import CACHE_TIMEOUT

# In-memory cache dictionary: {city_name: (timestamp, data)}
cache: Dict[str, Tuple[float, Any]] = {}


def get_from_cache(city: str) -> Any:
    """Retrieve weather data for a city from the cache if available and not expired.
    
    Args:
        city (str): Name of the city to retrieve data for
        
    Returns:
        Any: Cached weather data or None if not in cache or expired
    """
    if city.lower() not in cache:
        return None
    
    timestamp, data = cache[city.lower()]
    current_time = time.time()
    
    # Check if cache entry has expired
    if current_time - timestamp > CACHE_TIMEOUT:
        # Remove expired entry
        del cache[city.lower()]
        return None
    
    return data


def add_to_cache(city: str, data: Any) -> None:
    """Add or update weather data for a city in the cache.
    
    Args:
        city (str): Name of the city to cache data for
        data (Any): Weather data to cache
    """
    cache[city.lower()] = (time.time(), data)


def clear_cache() -> None:
    """Clear all entries from the cache."""
    cache.clear()


def get_cache_stats() -> Dict[str, Any]:
    """Get statistics about the current cache state.
    
    Returns:
        Dict[str, Any]: Dictionary containing cache statistics
    """
    current_time = time.time()
    active_entries = 0
    expired_entries = 0
    
    for city, (timestamp, _) in cache.items():
        if current_time - timestamp <= CACHE_TIMEOUT:
            active_entries += 1
        else:
            expired_entries += 1
    
    return {
        "total_entries": len(cache),
        "active_entries": active_entries,
        "expired_entries": expired_entries
    }