#!/usr/bin/env python3

import requests
import sqlite3
from datetime import datetime

API_KEY = "enter your api"
CITIES = [
    "Bengaluru",
    "Mumbai",
    "Delhi",
    "Chennai",
    "Hyderabad"
]

for CITY in CITIES:
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={CITY}&appid={API_KEY}&units=metric"
    )


response = requests.get(url)

if response.status_code != 200:
    raise Exception("API call failed")

data = response.json()

record = (
    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    data["name"],
    data["main"]["temp"],
    data["main"]["humidity"],
    data["main"]["pressure"]
)

conn = sqlite3.connect("weather.db")
cursor = conn.cursor()

cursor.execute("""
INSERT INTO weather_fact (
    load_time,
    city,
    temperature,
    humidity,
    pressure
)
VALUES (?, ?, ?, ?, ?)
""", record)

conn.commit()
conn.close()

print("Data inserted successfully!")
