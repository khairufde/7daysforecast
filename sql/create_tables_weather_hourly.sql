CREATE TABLE forecast.weather_hourly (
    id INT PRIMARY KEY,
    location_id INT REFERENCES forecast.locations(location_id),
    time TIMESTAMP NOT NULL,
    temperature_2m FLOAT,
    relative_humidity_2m FLOAT,
    wind_speed_10m FLOAT,
    wind_direction_10m FLOAT,
    wind_gusts_10m FLOAT,
    apparent_temperature FLOAT,
    precipitation_probability FLOAT,
    precipitation FLOAT,
    rain FLOAT,
    snowfall FLOAT
);