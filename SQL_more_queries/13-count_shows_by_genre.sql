-- Select the genre and count the number of shows linked to each genre

SELECT genres.name AS genre, COUNT(tv_show.id) AS number_of_shows
FROM tv_show_genres
INNER JOIN genres
ON tv_show_genres.genre_id = genre.id
GROUP BY genre
HAVING COUNT(tv_show_id) > 0
ORDER BY number_of_shows DESC;
