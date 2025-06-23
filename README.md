p {
  text-indent: 50px;
  
<h1>ETL 7 Days Forecast Weather Data</h1>

<h2>Description</h2>
<p>This is a dummy project that shows process fetches 7-day weather forecast data from the <a href="https://open-meteo.com/">open-meteo</a> API, transforms it to fit ERD, loads it into a PostgreSQL database, then make a dashboard and insight summary.
</p>
<h2>Project Background</h2>
<p>A company want to hold a 3-day outdoor event (1 day prep, 1 day event, 1 day cleanup) within the date range of May 29 – June 4, 2025. The goal is to identify 10 candidates cities in england with the lowest risk of rain, based on hourly precipitation probability forecasts, then select the best city.
</p>

<h2>Step-by-Step:</h2>

<h2>
1. Design ERD
</h2>
<p align="center">
<img src="https://raw.githubusercontent.com/khairufde/7daysforecast/refs/heads/main/erd/demo%20-%20forecast.png"/>
 
<h2>2. Create tables in PostgreSQL</h2>

- <b>SQL file for creating locations table: <a href="https://github.com/khairufde/7daysforecast/blob/main/sql/create_tables_locations.sql">forecast.locations</a></b>
- <b>SQL file for creating weather_hourly table: <a href="https://github.com/khairufde/7daysforecast/blob/main/sql/create_tables_weather_hourly.sql">forecast.weather_hourly</a></b>

<h2>3. Extract, transform, and load data into Postgresql</h2>

- <b>Folder scripts of ETL process: <a href="https://github.com/khairufde/7daysforecast/tree/main/scripts">Python scripts</a></b>

<h2>5. Data in PostgreSQL</h2>

<p align="center">
forecast.locations<br/>
<img src="https://raw.githubusercontent.com/khairufde/7daysforecast/refs/heads/main/table_pic/demo%20-%20forecast%20-%20locations.PNG"/>
<p align="center">
forecast.weather_hourly<br/>
<img src="https://raw.githubusercontent.com/khairufde/7daysforecast/refs/heads/main/table_pic/demo%20-%20forecast%20-%20weather_hourly.PNG"/>

<h2>6. Creating Dashboard</h2>

- <b>Dynamic Dashboard Link: <a href="https://public.tableau.com/views/PrecipitationProbabilityinEngland/HRP?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link">Chance of Rain per Hour in England</a></b>

<h2>Key Insight</h2>

From the forecast data (May 29 – June 4, 2025):
<br />

Best Overall Options:
<br />

<p>London and Southampton showed a low chance of rain (<70%) across all 7 days, making them the most reliable choices for an outdoor event.</p>
<br />

Moderate Options (Good 3-day windows: May 30 – June 2):
<br />

- <b>Birmingham</b>
- <b>Leeds</b>
- <b>Nottingham</b>
- <b>Bristol</b>
- <b>Manchester</b>
- <b>Sheffield</b>
- <b>Newcastle</b>
<br />

Not Recommended:
<br />

<p>Liverpool have fluktuatif precipitation probabilty and did not have 3 consecutive low precipitation probability, sometimes the probability close to or surpases 70%, making it a high-risk choice.</p>
<br />

<h2>Technologies:</h2>

<b/>
1. Python (Pandas, SQLAlchemy, requests_cache)
<br/>
<b/>
2. <a href="https://open-meteo.com/">open-meteo</a>
<br/>
<b/>
3. PostgreSQL
<br/>
<b/>
4. DBeaver
<br/>

<h2>How To Run:</h2>

<b/>
1. Configure your .env file with your authentication (remove .example in .env files name).
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

