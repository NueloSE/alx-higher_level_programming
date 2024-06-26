-- A script that displays the top 3 of cities temperature during
-- during july and august ordered by temperature

SELECT
    city,
    SUM(value) / COUNT(*) AS avg_temp
FROM temperatures
WHERE month = '7' OR month = '8'
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
