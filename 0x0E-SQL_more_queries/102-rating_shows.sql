-- sql query that list all shows with their rating
SELECT tv_shows.title, tv_show_ratings.rate
FROM tv_shows
JOIN tv_show_ratings ON tv_shows.id=tv_show_ratings
ORDER BY tv_show_ratings.rate DESC;
