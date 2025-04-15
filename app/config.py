"""Configuration module for the Weather Proxy API.

This module loads environment variables from a .env file using python-dotenv.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get OpenWeatherMap API key from environment variables
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

# API base URL
OPENWEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Cache timeout in seconds (10 minutes)
CACHE_TIMEOUT = 600