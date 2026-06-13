#!/usr/bin/env python3
import requests

API_KEY = "2a1179a0e22aac39d436635997069e09"

CITY = "Bengaluru"

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