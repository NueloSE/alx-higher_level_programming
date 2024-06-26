-- Import the database dump from hbtn_0d_tvshows to your MySQL server: https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql

-- Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.

-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT
	name AS genre,
	COUNT(genre_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY name
ORDER BY number_of_shows DESC;
