-- Write a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter

-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use a maximum of two SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT name
FROM tv_genres
WHERE id NOT IN
	(SELECT genre_id
	FROM tv_show_genres tsg
	WHERE show_id = '8')
ORDER BY name;
