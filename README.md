# 🌦️ API-Based Weather Data ETL Pipeline

An end-to-end data pipeline designed to ingest, transform, and store real-time global weather metrics. This project demonstrates a production-ready workflow using containerization and modern data storage formats.

## 🚀 Tech Stack
* **Language:** Python 3.12+ (Pandas, Requests, Psycopg2)
* **Infrastructure:** Docker & Docker Compose
* **Database:** PostgreSQL
* **Storage Format:** Apache Parquet (Optimized for OLAP)
* **Security:** Python-dotenv (Environment Variable Management)

## 🛠️ Data Pipeline Architecture

1. **Extraction:** Robust ingestion of nested JSON data from the OpenWeatherMap API.
2. **Transformation:** Data cleaning and normalization using **Pandas**. Key metrics (Temperature, Humidity, Wind Speed) are extracted and timestamps are converted to ISO format.
3. **Loading:** * **Relational:** Data is upserted into a **PostgreSQL** instance for transactional integrity.
    * **Analytical:** Data is mirrored into **Snappy-compressed Parquet** files, reducing storage footprint and enabling high-performance analytical queries.



## 📦 Setup & Installation

### 1. Prerequisites
- Docker & Docker Compose
- OpenWeatherMap API Key

### 2. Configuration
Create a `.env` file in the root directory and add the following keys (replace placeholders with your actual credentials):

```bash
API_KEY=your_openweathermap_api_key
DB_NAME=weather_db
DB_USER=postgres
DB_PASSWORD=your_secure_password
DB_HOST=localhost
DB_PORT=5432