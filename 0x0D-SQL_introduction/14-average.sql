-- A script that computes the score average of all records in second_table

SELECT SUM(score) / COUNT(score) AS average
FROM second_table
