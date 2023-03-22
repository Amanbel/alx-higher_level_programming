-- sql query that displays the comedy genre shows
SELECT title
FROM tv_shows
JOIN tv_show_genres ON id=tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id=tv_genres.id
WHERE tv_genres.name="Comedy"
ORDER BY title;
