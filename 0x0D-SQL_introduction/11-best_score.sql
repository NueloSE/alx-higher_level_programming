-- A script that lists all records with a score >= 10 in the second_table in hbtn_0c_0

SELECT
    score,
    name
FROM second_table
WHERE score >= '10'
ORDER BY score DESC
