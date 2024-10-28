-- Write a script that lists all Comedy shows in the database hbtn_0d_tvshows

SELECT tv_shows.title AS title FROM tv_genres
LEFT JOIN tv_show_genres
ON tv_show_genres.genre.id = tv_genre.id
WHERE tv_genres.name = 'Comedy'
ORDER BY title;