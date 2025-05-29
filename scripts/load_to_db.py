import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

def get_engine_from_env(env_path="../.env"):
    env_path = os.path.abspath(env_path)
    if not os.path.exists(env_path):
        raise FileNotFoundError(f".env file not found at: {env_path}")
    
    load_dotenv(dotenv_path=env_path)
    db_url = os.getenv("DATABASE_URL")
    
    if not db_url:
        raise ValueError("DATABASE_URL not found in .env file")
    
    return create_engine(db_url)

def load_locations_to_db(locations_df, engine):
    try:
        locations_df.to_sql(
            "locations",
            engine,
            schema="forecast",
            if_exists="append",
            index=False,
            chunksize=1000
        )
        print("Locations table loaded successfully.")
    except Exception as e:
        print("Error loading locations to DB:", e)

def load_weather_to_db(weather_df, engine):
    try:
        weather_df.to_sql(
            "weather_hourly",
            engine,
            schema="forecast",
            if_exists="append",
            index=False,
            chunksize=1000
        )
        print("Weather table loaded successfully.")
    except Exception as e:
        print("Error loading weather data to DB:", e)

def export_table_to_csv(engine, table_name, output_path):
    try:
        df = pd.read_sql(f"SELECT * FROM forecast.{table_name}", engine)
        df.to_csv(output_path, index=False)
        print(f"Exported {table_name} to {output_path}")
    except Exception as e:
        print(f"Error exporting {table_name} to CSV:", e)
