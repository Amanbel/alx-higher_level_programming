-- sql query to show name of genres of tv shows not including Dexter
SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.id NOT IN (
	SELECT tv_genres.id
	FROM tv_genres
	JOIN tv_show_genres ON tv_show_genres.genre_id=tv_genres.id
	JOIN tv_shows ON tv_shows.id=tv_show_genres.show_id
	WHERE tv_shows.title="Dexter")
ORDER BY tv_genres.name;
