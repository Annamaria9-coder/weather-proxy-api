import pytest
import asyncio
from fastapi.testclient import TestClient
from fastapi import status
from app.main import app

# Create a test client
client = TestClient(app)

# ✅ TEMP TEST: Make sure pytest is working with async
def test_dummy_async_runs():
    assert True


# ✅ Sample test for a valid city (with mocked response)
def test_get_weather_valid_city(monkeypatch):
    mock_response = {
        "city": "London",
        "country": "GB",
        "temperature": {
            "kelvin": 289.5,
            "celsius": 16.35,
            "fahrenheit": 61.43
        },
        "weather": {
            "main": "Clouds",
            "description": "few clouds",
            "icon": "02d"
        },
        "details": {
            "humidity": 65,
            "pressure": 1012,
            "wind_speed": 3.5,
            "clouds": 40
        },
        "custom_message": "It's cool outside. It's cloudy today."
    }

    def mock_get_weather_data(city: str, use_cache: bool = True):
        return mock_response

    from app import weather
    monkeypatch.setattr(weather, "get_weather_data", mock_get_weather_data)

    response = client.get(f"/weather/London")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["city"] == "London"
    assert "custom_message" in response.json()


# ✅ Test for invalid city (simulate a 404 error)
def test_get_weather_invalid_city(monkeypatch):
    def mock_weather_failure(city: str, use_cache: bool = True):
        raise ValueError("City not found.")

    from app import weather
    monkeypatch.setattr(weather, "get_weather_data", mock_weather_failure)

    response = client.get("/weather/Fakeville")
    assert response.status_code == 404
    assert response.json()["error"] == "City 'Fakeville' not found"