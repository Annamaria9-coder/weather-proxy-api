# 📘 Conceptual Design: Weather Proxy API

This project was designed for a backend assessment. The goal was to build a fast, reliable API that fetches weather data, transforms it, and adds human-readable logic — all while being production-aware (caching, error handling, Docker, etc.).

---

### 🌤️ API Selection

I chose **OpenWeatherMap** because it’s stable, fast, and easy to work with. It allowed me to search by city, get structured JSON, and focus on backend logic rather than wrestling with an external API.  
It also returns conditions in a format I could easily map to friendly categories like “sunny” or “rainy”.

---

### 🔁 Data Transformation

The API gives a lot of data — but I trimmed it down to what users actually care about:


{
  "city": "Nairobi",
  "temperature": 26,
  "condition": "sunny",
  "custom_message": "Great day for a walk."
}

I also normalized weather terms (like “Drizzle” → “Rainy”) to keep tone consistent. The API was built to feel ready for use in apps or dashboards — no extra filtering needed.

⸻

🧠 Business Logic Mapping

Weather isn’t just data — it’s something people feel. I added a layer of logic that maps conditions to short, human messages:

Condition	Message
Clear	Great day for a walk.
Rain	Don’t forget your umbrella.
Snow	Time for some hot cocoa.
Thunderstorm	Might want to stay indoors.
Clouds	A calm, cloudy day.
Drizzle	Light rain — maybe bring a hoodie.
Mist / Fog	Low visibility — stay sharp.
Unknown	Stay safe out there.



⸻

💾 Caching Strategy

Every city’s weather is cached for 10 minutes. This reduces API calls, makes things faster, and protects the app from external service failures.
	•	🧠 In-Memory (default): Quick to set up, great for local or solo use.
	•	🧱 Redis (via Docker): Better for production or shared deployments. Optional but included.

If Redis is running, the app uses it. If not, it falls back to memory — no config required.

⸻

❗ Error Handling

I wanted this app to handle weird inputs gracefully — not just crash.
	•	Missing city → 400 Bad Request with helpful message
	•	Invalid city → 404 Not Found with “City not found.”
	•	API timeout/down → 503 Service Unavailable with a fallback message
	•	Unknown error → 500 Internal Server Error with generic message

⸻

🔧 Optional Enhancements
	•	✅ Swagger UI (built-in via FastAPI)
	•	✅ Health check at /health
	•	✅ Docker & Docker Compose support
	•	✅ Postman & curl testing helpers
	•	✅ Async requests (using httpx)
	•	✅ Secure API keys with .env variables

⸻

🧭 Diagram

A full conceptual flow is visualized here:
🔗 Weather Proxy Architecture Diagram

⸻

💬 Final Note

I didn’t want to just make something that runs — I wanted to make something clear, solid, and ready to build on. Even though I’m submitting this late, I made sure every decision was intentional, from error handling to caching to user experience.

⸻

☁️ Weather Proxy API

A lightweight proxy API built with FastAPI that fetches current weather data from OpenWeatherMap, simplifies the response, adds custom human-readable messages, and implements caching to reduce redundant API calls.

This project was developed as part of a backend development take-home assessment. It’s designed to be simple, clear, and production-conscious — with thoughtful error handling, extensibility, and developer-friendly setup.

⸻

🚀 Features
	•	🔹 Real-time weather data from OpenWeatherMap
	•	🔹 Simplified API response with essential weather info only
	•	🔹 Custom weather messages based on temperature and conditions
	•	🔹 In-memory caching (with optional Redis support)
	•	🔹 Cache stats and clearing endpoints
	•	🔹 Async HTTP requests using httpx
	•	🔹 Environment variable management via .env
	•	🔹 Swagger docs (auto-generated via FastAPI)
	•	🔹 Docker-ready setup (optional)
	•	🔹 Basic error handling for invalid input and API timeouts
	•	🔹 Health check endpoint for uptime monitoring

⸻

🧱 Project Structure

weather-proxy-api/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app and route definitions
│   ├── config.py        # Loads environment variables
│   ├── cache.py         # Caching logic (in-memory / Redis)
│   ├── weather.py       # External API request logic
│   └── utils.py         # Helpers for messages, temperature conversion
├── .env.example         # Sample environment config
├── Dockerfile           # Container setup
├── docker-compose.yml   # Runs app + Redis together
├── requirements.txt     # Python dependencies
└── README.md            # This file



⸻

⚙️ Setup Instructions

✅ Prerequisites
	•	Python 3.8+
	•	OpenWeatherMap API key (get one at https://openweathermap.org/api)
	•	(Optional) Docker & Docker Compose if running with Redis

⸻

🔧 Local Installation

# 1. Clone the repo
git clone https://github.com/your-username/weather-proxy-api.git
cd weather-proxy-api

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create .env file
echo "OPENWEATHER_API_KEY=your_key_here" > .env

# 4. Run the API
uvicorn app.main:app --reload

Visit http://localhost:8000/docs for interactive Swagger UI.

⸻

🐳 Docker Setup (Optional)

To run the API along with Redis:

docker-compose up --build

This will:
	•	Build and run the FastAPI app
	•	Launch Redis for caching
	•	Auto-load your .env variables

⸻

🌐 API Endpoints

✅ GET /weather/{city}

Returns current weather for a city with custom message.

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

Returns stats about cached entries.

⸻

🧹 DELETE /cache/clear

Clears all cached entries.

⸻

🩺 GET /health

Simple health check endpoint.

⸻

🧪 Testing the API

curl http://localhost:8000/weather/Nairobi

Or use:
	•	Swagger UI at /docs
	•	Postman collection (optional)

⸻

📜 License

MIT

---

