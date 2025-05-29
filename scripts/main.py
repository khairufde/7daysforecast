import pandas as pd
from fetch_weather import fetch_hourly_weather
from load_to_db import (
    get_engine_from_env,
    load_locations_to_db,
    load_weather_to_db,
    export_table_to_csv
)

locations_df = pd.read_csv("../data/locations.csv")
locations = locations_df.to_dict(orient="records")

weather_df, locations_df = fetch_hourly_weather(locations)

engine = get_engine_from_env()

load_locations_to_db(locations_df, engine)
load_weather_to_db(weather_df, engine)

export_table_to_csv(engine, "locations", "../data/locations.csv")
export_table_to_csv(engine, "weather_hourly", "../data/weather_hourly.csv")

print("Complete.")
