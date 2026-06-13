#!/usr/bin/env python3
import requests
import os

API_KEY = os.getenv("OPENWEATHER_API_KEY")
if not API_KEY:
    raise EnvironmentError(
        "Please set the OPENWEATHER_API_KEY environment variable with your OpenWeatherMap API key."
    )

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

data = response.json()

city = data["name"]
temperature = data["main"]["temp"]
humidity = data["main"]["humidity"]
pressure = data["main"]["pressure"]

weather_record = {

    "city": city,
    "temperature": temperature,
    "humidity": humidity,
    "pressure": pressure
}

print(weather_record)