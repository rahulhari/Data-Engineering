import sqlite3
#!/usr/bin/env python3

conn = sqlite3.connect("weather.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS weather_fact (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    load_time TEXT,
    city TEXT,
    temperature REAL,
    humidity INTEGER,
    pressure INTEGER
)
""")

conn.commit()
conn.close()

print("Database and table created successfully!")
