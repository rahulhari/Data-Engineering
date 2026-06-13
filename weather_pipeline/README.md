# Weather Pipeline

A simple Python data engineering project that extracts current weather data for Bengaluru from the OpenWeatherMap API and loads it into CSV and SQLite outputs.

## Project Structure

```text
weather_pipeline/
├── create_db.py          # Creates the SQLite database table
├── weather_extract.py    # Extracts and prints weather data
├── weather_load_csv.py   # Extracts weather data and appends it to CSV
├── weather_load_db.py    # Extracts weather data and inserts it into SQLite
├── view_data.py          # Reads and prints rows from SQLite
├── weather_data.csv      # CSV output file
└── weather.db            # SQLite database file
```

## What It Collects

Each weather record contains:

- `load_time`
- `city`
- `temperature`
- `humidity`
- `pressure`

## Requirements

- Python 3
- `requests`
- `pandas`

Install dependencies:

```bash
python3 -m pip install requests pandas
```

On some systems, `pip` may not work directly. Use `python3 -m pip` or `pip3` instead.

## How To Run

Move into the project folder first:

```bash
cd weather_pipeline
```

Create the SQLite database and table:

```bash
python3 create_db.py
```

Extract and print current weather data:

```bash
python3 weather_extract.py
```

Load weather data into the CSV file:

```bash
python3 weather_load_csv.py
```

Load weather data into the SQLite database:

```bash
python3 weather_load_db.py
```

View records stored in SQLite:

```bash
python3 view_data.py
```

## Output

CSV data is saved to:

```text
weather_pipeline/weather_data.csv
```

SQLite data is saved to:

```text
weather_pipeline/weather.db
```

The SQLite table name is:

```text
weather_fact
```

## API Configuration

The scripts currently use OpenWeatherMap and are configured for:

```python
CITY = "Bengaluru"
```

To use a different city, update the `CITY` value in the scripts.

For better security, avoid committing real API keys directly in code. A future improvement would be to load the API key from an environment variable.

## Notes

- Run the scripts from inside the `weather_pipeline` folder because the CSV and database paths are relative.
- `weather_load_csv.py` appends new rows to `weather_data.csv`.
- `weather_load_db.py` inserts new rows into the `weather_fact` table.
