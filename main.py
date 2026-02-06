import os
import requests
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def fetch_weather(city):
    api_key = os.getenv("WEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        }
    return None


def save_to_db(weather_data):
    try:
        # Connect to the Dockerized Postgres
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        cur = conn.cursor()

        # Create the table if it doesn't exist yet
        cur.execute("""
            CREATE TABLE IF NOT EXISTS weather (
                id SERIAL PRIMARY KEY,
                city VARCHAR(50),
                temp FLOAT,
                humidity INT,
                description VARCHAR(100),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)

        # Insert the data
        insert_query = """
            INSERT INTO weather (city, temp, humidity, description)
            VALUES (%s, %s, %s, %s)
        """
        cur.execute(insert_query, (
            weather_data['city'],
            weather_data['temperature'],
            weather_data['humidity'],
            weather_data['description']
        ))

        conn.commit()
        print(f"Successfully saved weather for {weather_data['city']} to the database!")

        cur.close()
        conn.close()
    except Exception as e:
        print(f"Database error: {e}")



if __name__ == "__main__":
    cities = ["London", "New York", "Tokyo", "Dubai", "Lahore"]

    print(f"Starting pipeline for {len(cities)} cities...")

    for city in cities:
        weather = fetch_weather(city)
        if weather:
            save_to_db(weather)

    print("Pipeline execution complete.")