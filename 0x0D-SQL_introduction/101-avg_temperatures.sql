-- A script that displays the average temperature by city ordered by temperature

SELECT
    city,
    SUM(value) / COUNT(*) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
