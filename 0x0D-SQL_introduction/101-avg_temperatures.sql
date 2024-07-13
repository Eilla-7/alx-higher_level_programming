-- Query to calculate average temperature in Fahrenheit by city
SELECT city, ROUND(AVG(temperature) * 1.8 + 32, 2) AS avg_temperature_fahrenheit
FROM weather_data
GROUP BY city
ORDER BY avg_temperature_fahrenheit DESC;
