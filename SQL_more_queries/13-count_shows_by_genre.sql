-- Script to list all genres and the number of shows linked to each from hbtn_0d_tvshows database
-- Each record displays: <TV Show genre> - <Number of shows linked to this genre>
-- First column must be called genre
-- Second column must be called number_of_shows
-- Don't display a genre that doesn't have any shows linked
-- Results are sorted in descending order by the number of shows linked.

SELECT genres.name AS genre, COUNT(tv_shows.id) AS number_of_shows
FROM genres
JOIN tv_show_genres
ON genres.id = tv_show_genres.genre_id
JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
GROUP BY genres.name
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;