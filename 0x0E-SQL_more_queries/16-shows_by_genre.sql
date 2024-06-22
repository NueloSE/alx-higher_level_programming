-- A script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.

-- If a show doesn’t have a genre, display NULL in the genre column
-- Each record should display: tv_shows.title - tv_genres.name
-- Results must be sorted in ascending order by the show title and genre name
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT
	title,
	name
FROM tv_show_genres tsg
JOIN tv_genres tg ON tsg.genre_id = tg.id
RIGHT JOIN tv_shows ts ON tsg.show_id = ts.id
ORDER BY title ASC, name ASC;

