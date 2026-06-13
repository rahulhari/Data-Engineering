#!/usr/bin/env python3
import requests
import pandas as pd
import os
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
data = response.json()

if response.status_code != 200:
    raise Exception("API call failed")

if "main" not in data:
    raise Exception("Weather data missing")

weather_record = {
    "load_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "city": data["name"],
    "temperature": data["main"]["temp"],
    "humidity": data["main"]["humidity"],
    "pressure": data["main"]["pressure"]
}

df = pd.DataFrame([weather_record])

file_name = "weather_data.csv"

if os.path.exists(file_name):
    df.to_csv(file_name, mode="a", header=False, index=False)
else:
    df.to_csv(file_name, index=False)

print("Data loaded successfully!")
print(weather_record)
