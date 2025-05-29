import pandas as pd
import openmeteo_requests
import requests_cache
from retry_requests import retry

def fetch_hourly_weather(locations):
    hourly_vars = [
        "temperature_2m", "relative_humidity_2m", "wind_speed_10m",
        "wind_direction_10m", "wind_gusts_10m", "apparent_temperature",
        "precipitation_probability", "precipitation", "rain", "snowfall"
    ]

    # Setup Open-Meteo client with retry and cache
    cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
    retry_session = retry(cache_session, retries=3, backoff_factor=0.2)
    client = openmeteo_requests.Client(session=retry_session)

    locations_list = []
    weather_rows = []

    for loc_id, loc in enumerate(locations, start=1):
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": loc["lat"],
            "longitude": loc["lon"],
            "hourly": hourly_vars,
            "timezone": "Europe/London"
        }

        responses = client.weather_api(url, params=params)
        response = responses[0]

        hourly = response.Hourly()
        time_index = pd.date_range(
            start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
            end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
            freq=pd.Timedelta(seconds=hourly.Interval()),
            inclusive="left"
        )

        # Build variable arrays into columns
        data = {"location_id": loc_id, "time": time_index}
        for i, var in enumerate(hourly_vars):
            data[var] = hourly.Variables(i).ValuesAsNumpy()

        df_weather = pd.DataFrame(data)
        weather_rows.append(df_weather)

        locations_list.append({
            "location_id": loc_id,
            "name": loc["name"],
            "latitude": loc["lat"],
            "longitude": loc["lon"]
        })

    weather_df = pd.concat(weather_rows, ignore_index=True)
    locations_df = pd.DataFrame(locations_list)

    weather_df = weather_df.applymap(lambda x: x.item() if hasattr(x, "item") else x)

    return weather_df, locations_df
