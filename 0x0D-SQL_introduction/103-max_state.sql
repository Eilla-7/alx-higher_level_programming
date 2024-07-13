-- Query to find max temperature of each state ordered by State name
SELECT state, MAX(temperature) AS max_temperature
FROM weather_data
GROUP BY state
ORDER BY state;
