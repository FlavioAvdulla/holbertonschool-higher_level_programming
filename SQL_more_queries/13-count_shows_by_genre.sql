-- Select the genre and count the number of shows linked to each genre
SELECT genre, COUNT(tv_show_id) AS number_of_shows
FROM tv_shows_genres
INNER JOIN genres
ON tv_shows_genres.genre_id = genres.id
GROUP BY genre
HAVING COUNT(tv_show_id) > 0
ORDER BY number_of_shows DESC;