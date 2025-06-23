<h1>ETL 7 Days Forecast Weather Data</h1>

<h2>Description</h2>
This is a dummy project that shows process fetches 7-day weather forecast data from the <a href="https://open-meteo.com/">open-meteo</a> API, transforms it to fit ERD, loads it into a PostgreSQL database, then make a dashboard and insight summary.
<br />
<h2>Project Background</h2>
A company want to hold a 3-day outdoor event (1 day prep, 1 day event, 1 day cleanup) within the date range of May 29 – June 4, 2025. The goal is to identify 10 candidates cities in england with the lowest risk of rain, based on hourly precipitation probability forecasts, then select the best city.
<br />

<h2>Step-by-Step:</h2>

<b/>
1. Design ERD <img src="https://raw.githubusercontent.com/khairufde/7daysforecast/refs/heads/main/erd/demo%20-%20forecast.png">
<br/>
<b/>
<img src="https://raw.githubusercontent.com/khairufde/7daysforecast/refs/heads/main/erd/demo%20-%20forecast.png">
<br/>
<b/>
2. Create tables in PostgreSQL
<br/>
<b/>
3. Fetch data from <a href="https://open-meteo.com/">open-meteo</a>
<br/>
<b/>
4. Transform data
<br/>
<b/>
5. Load data into PostgreSQL
<br/>

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

