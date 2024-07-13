-- Query to find top 3 cities with highest temperatures during July and August
SELECT city, MAX(temperature) AS max_temperature
FROM weather_data
WHERE MONTH(date) IN (7, 8)
GROUP BY city
ORDER BY max_temperature DESC
LIMIT 3;
