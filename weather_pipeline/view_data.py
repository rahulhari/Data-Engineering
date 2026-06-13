#!/usr/bin/env python3
import sqlite3

conn = sqlite3.connect("weather.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM weather_fact")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()

