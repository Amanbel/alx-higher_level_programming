-- sql query to display tv show genre and the number of shows
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres
ON tv_genres.id=tv_show_genres.genre_id
ORDER BY COUNT(tv_show_genres.show_id) DESC;
