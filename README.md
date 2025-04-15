
# ☁️ Weather Proxy API

A lightweight proxy API built with FastAPI that fetches current weather data from OpenWeatherMap, simplifies the response, adds custom human-readable messages, and implements caching to reduce redundant API calls.

This project was developed as part of a backend development take-home assessment. It’s designed to be simple, clear, and production-conscious — with thoughtful error handling, extensibility, and developer-friendly setup.

---

## 🚀 Features

- 🔹 **Real-time weather data** from OpenWeatherMap
- 🔹 **Simplified API response** with essential weather info only
- 🔹 **Custom weather messages** based on temperature and conditions
- 🔹 **In-memory caching** (with optional Redis support)
- 🔹 **Cache stats and clearing endpoints**
- 🔹 **Async HTTP requests** using `httpx`
- 🔹 **Environment variable management** via `.env`
- 🔹 **Swagger docs** (auto-generated via FastAPI)
- 🔹 **Docker-ready setup** (optional)
- 🔹 **Basic error handling for invalid input and API timeouts**
- 🔹 **Health check endpoint** for uptime monitoring

---

## 🧱 Project Structure

weather-proxy-api/
├── app/
│   ├── init.py
│   ├── main.py        # FastAPI app and route definitions
│   ├── config.py      # Loads environment variables
│   ├── cache.py       # Caching logic (in-memory / Redis)
│   ├── weather.py     # External API request logic
│   └── utils.py       # Helpers for messages, temperature conversion
├── .env               # API keys and config variables
├── Dockerfile         # Container setup
├── docker-compose.yml # Runs app + Redis together (optional)
├── requirements.txt   # Python dependencies
└── README.md          # You’re reading it :)

---

## ⚙️ Setup Instructions

### ✅ Prerequisites

- Python 3.8+
- An OpenWeatherMap API key (get one here: https://openweathermap.org/api)
- (Optional) Docker & Docker Compose if running with Redis

---

### 🔧 Local Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/weather-proxy-api.git
   cd weather-proxy-api

	2.	Install dependencies:

pip install -r requirements.txt


	3.	Create your .env file:

OPENWEATHER_API_KEY=your_api_key_here


	4.	Run the API:

uvicorn app.main:app --reload



Visit http://localhost:8000/docs to interact with the Swagger UI.

⸻

🐳 Docker Setup (Optional)

To run the API along with Redis:

docker-compose up --build

This will:
	•	Build and run the FastAPI app
	•	Launch Redis for caching (port 6379)
	•	Auto-load your .env variables

⸻

🌐 API Endpoints

✅ GET /weather/{city}

Returns current weather for a city with custom message and simplified structure.

Example:

GET /weather/London

Response:

{
  "city": "London",
  "country": "GB",
  "temperature": {
    "kelvin": 287.07,
    "celsius": 13.9,
    "fahrenheit": 57.1
  },
  "weather": {
    "main": "Clouds",
    "description": "overcast clouds",
    "icon": "04d"
  },
  "details": {
    "humidity": 88,
    "pressure": 994,
    "wind_speed": 3.6,
    "clouds": 99
  },
  "custom_message": "It's cool outside. It's cloudy today."
}



⸻

⚙️ GET /cache/stats

Returns stats about how many cities are cached and how many entries have expired.

⸻

🧹 DELETE /cache/clear

Clears all cached weather entries.

⸻

🩺 GET /health

A small endpoint to check if the app is alive.

⸻

💬 Custom Message Mapping

Weather conditions are mapped to short, user-friendly messages:

Condition	Message
Clear	Great day for a walk.
Rain	Don’t forget your umbrella.
Snow	Time for some hot cocoa.
Thunderstorm	Might want to stay indoors today.
Clouds	A calm, cloudy day.
Drizzle	Light rain today — maybe bring a hoodie.
Mist / Fog	Low visibility — stay sharp out there.
Unknown	Stay safe out there.



⸻

🧪 Testing the API

You can test the API with curl:

curl http://localhost:8000/weather/Nairobi

Or interactively using:
	•	Swagger docs at /docs
	•	Postman (collection included optionally)

⸻

🧼 Notes
	•	If Redis is unavailable, the API defaults to in-memory caching.
	•	Caching is per city and expires after 10 minutes.
	•	API responses are intentionally simplified to avoid clutter and improve clarity.

⸻

📜 License

This project is open-sourced under the MIT license.
