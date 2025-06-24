
<h1>ETL 7 Days Forecast Weather Data</h1>

<h2>Description</h2>
This is a dummy project that shows process fetches 7-day weather forecast data from the non-commercial <a href="https://open-meteo.com/">open-meteo</a> API, transforms it to fit ERD, loads it into a PostgreSQL database, then make a dashboard and insight summary.
<br />
<h2>Project Background</h2>
A company want to hold a 3-day outdoor event (1 day prep, 1 day event, 1 day cleanup) within the date range of May 29 – June 4, 2025. The goal is to identify 10 candidates cities in england with the lowest risk of rain, based on hourly precipitation probability forecasts, then select the best city.
<br />

<h2>List of Cities</h2>

| No | City         | Latitude  | Longitude |
|----|--------------|-----------|-----------|
| 1  | London       | 51.5074   | -0.1278   |
| 2  | Manchester   | 53.4808   | -2.2426   |
| 3  | Birmingham   | 52.4862   | -1.8904   |
| 4  | Leeds        | 53.8008   | -1.5491   |
| 5  | Liverpool    | 53.4084   | -2.9916   |
| 6  | Newcastle    | 54.9783   | -1.6178   |
| 7  | Sheffield    | 53.3811   | -1.4701   |
| 8  | Bristol      | 51.4545   | -2.5879   |
| 9  | Nottingham   | 52.9548   | -1.1581   |
| 10 | Southampton  | 50.9097   | -1.4043   |

<h2>Step-by-Step:</h2>

<h3>1. Design ERD</h3>
<p align="center">
<img src="https://raw.githubusercontent.com/khairufde/7daysforecast/refs/heads/main/erd/demo%20-%20forecast.png"/>
 
<h3>2. Create tables in PostgreSQL</h3>

- <b>SQL file for creating locations table:<br />
  <a href="https://github.com/khairufde/7daysforecast/blob/main/sql/create_tables_locations.sql">forecast.locations</a><br />
- <b>SQL file for creating weather_hourly table:<br />
  <a href="https://github.com/khairufde/7daysforecast/blob/main/sql/create_tables_weather_hourly.sql">forecast.weather_hourly</a><br />

<h3>3. Extract, transform, and load data into Postgresql</h3>

- <b>Folder scripts of ETL process:<br />
  <a href="https://github.com/khairufde/7daysforecast/tree/main/scripts">Python scripts</a><br />

<h3>5. Data in PostgreSQL</h3>

  forecast.locations:<br/>
<p align="center">
<img src="https://raw.githubusercontent.com/khairufde/7daysforecast/refs/heads/main/table_pic/demo%20-%20forecast%20-%20locations.PNG"/>

  forecast.weather_hourly:<br/>
<p align="center">
<img src="https://raw.githubusercontent.com/khairufde/7daysforecast/refs/heads/main/table_pic/demo%20-%20forecast%20-%20weather_hourly.PNG"/>

<h3>6. Creating Dashboard</h3>

- <b>Dynamic Dashboard Link:<br />
  <a href="https://public.tableau.com/views/PrecipitationProbabilityinLondonSouthampton_png/Dashboard?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link">Chance of Rain per Hour in England</a><br />

<h3>Key Insight</h3>

From the forecast data (May 29 – June 4, 2025):
<br />

- Best Overall Options:<br />
  **London** and **Southampton** showed a low chance of rain (<70%) across all 7 days, making them the most reliable choices for an outdoor event.<br />
<p align="center">
<img src="https://raw.githubusercontent.com/khairufde/7daysforecast/refs/heads/main/dashboard/London%20%26%20Southampton.PNG"/>

- Moderate Options (Good 3-day windows: May 30 – June 2):<br />
  - <b>Birmingham</b>
  - <b>Leeds</b>
  - <b>Nottingham</b>
  - <b>Bristol</b>
  - <b>Manchester</b>
  - <b>Sheffield</b>
  - <b>Newcastle</b>
<br />
<p align="center">
<img src="https://raw.githubusercontent.com/khairufde/7daysforecast/refs/heads/main/dashboard/Moderate%20Options.PNG"/>

- Not Recommended:<br />
  **Liverpool** have fluctuating precipitation probabilty and did not have 3 consecutive low precipitation probability, sometimes the probability close to or surpases 70%, making it a high-risk choice.<br />
<p align="center">
<img src="https://raw.githubusercontent.com/khairufde/7daysforecast/refs/heads/main/dashboard/worst-Liverpool.PNG"/>

<h3>Tools:</h3>

<b/>
1. Python (Pandas, SQLAlchemy, requests_cache)
<br/>
<b/>
2. non-commercial <a href="https://open-meteo.com/">open-meteo</a>
<br/>
<b/>
3. PostgreSQL
<br/>
<b/>
4. DBeaver
<br/>

<h2>How To Run the Scripts:</h2>

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

