<h1>ETL 7 Days Forecast Weather Data</h1>

<h2>Description</h2>
This is a dummy project that shows process fetches 7-day weather forecast data from the <a href="https://open-meteo.com/">open-meteo</a> API, transforms it to fit ERD, loads it into a PostgreSQL database, then make a dashboard and insight summary.
<br />
<h2>Project Background</h2>
A company want to hold a 3-day outdoor event (1 day prep, 1 day event, 1 day cleanup) within the date range of May 29 – June 4, 2025. The goal is to identify 10 candidates cities in england with the lowest risk of rain, based on hourly precipitation probability forecasts, then select the best city.
<br />

<h2>Step-by-Step:</h2>

<h2>
1. Design ERD
</h2>
<p align="center">
<img src="https://raw.githubusercontent.com/khairufde/7daysforecast/refs/heads/main/erd/demo%20-%20forecast.png"/>
 
<h2>
2. Create tables in PostgreSQL
</h2>
<b/>
- File sql for creating locations table: <a href="https://github.com/khairufde/7daysforecast/blob/main/sql/create_tables_locations.sql">forecast.locations</a>
<br/>
<b/>
- File sql for creating weather_hourly table: <a href="https://github.com/khairufde/7daysforecast/blob/main/sql/create_tables_weather_hourly.sql">forecast.weather_hourly</a>
<br/>

<b/>
3. Fetch data from <a href="https://open-meteo.com/">open-meteo</a>
<br/>
<b/>
4. Transform data
<br/>

<h2>
5. Load data into PostgreSQL
</h2>
<p align="center">
forecast.locations<br/>
<img src="https://raw.githubusercontent.com/khairufde/7daysforecast/refs/heads/main/table_pic/demo%20-%20forecast%20-%20locations.PNG"/>
<p align="center">
forecast.weather_hourly<br/>
<img src="https://raw.githubusercontent.com/khairufde/7daysforecast/refs/heads/main/table_pic/demo%20-%20forecast%20-%20weather_hourly.PNG"/>

<h2>Technologies:</h2>

<b/>
1. Python (Pandas, SQLAlchemy, requests_cache)
<br/>
<b/>
2. <a href="https://open-meteo.com/">open-meteo</a>
<br/>
<b/>
3. PostgreSQL on AWS RDS
<br/>
<b/>
4. DBeaver
<br/>

<h2>How To Run:</h2>

<b/>
1. Configure your .env file with your AWS RDS database connection string (remove .example in .env files name).
<br/>
<b/>
2. Run main.py script
<br/>

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>

