# API-Based Weather Data Pipeline (Dockerized)

An automated data pipeline that fetches real-time weather data from OpenWeatherMap API, cleanses it using Python, and stores it in a containerized PostgreSQL database.

## 🚀 Tech Stack
* **Language:** Python 3.x
* **Database:** PostgreSQL (Dockerized)
* **Tools:** Docker, Docker Compose, REST API
* **Libraries:** Requests, Psycopg2, Python-dotenv

## 🛠️ Architecture
1. **Ingestion:** Python script fetches JSON data from OpenWeatherMap API.
2. **Transformation:** Data is filtered for key metrics (Temp, Humidity, Description).
3. **Storage:** Cleaned data is upserted into a PostgreSQL database running in a Docker container.

## 📦 Setup & Installation
1. Clone the repository.
2. Create a `.env` file with your `WEATHER_API_KEY`.
3. Run `docker-compose up -d` to start the database.
4. Run `pip install -r requirements.txt`.
5. Execute `python main.py` to run the pipeline.