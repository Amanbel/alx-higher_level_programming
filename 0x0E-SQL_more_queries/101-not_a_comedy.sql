-- sql query to show tv_shows title with out comedy
SELECT title
FROM tv_shows
ORDER BY title

MINUS

SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_show_genres.show_id=tv_shows.id
JOIN tv_genres ON tv_show_genres.genre_id=tv_genres.id
WHERE tv_genres.name!="Comedy"
ORDER BY title
