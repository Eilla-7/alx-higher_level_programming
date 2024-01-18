-- List genres from hbtn_0d_tvshows with the number of shows linked to each genre
SELECT tv_genres.name AS 'genre', COUNT(tv_show_genres.genre.id) AS 'number_of_shows'
FROM tv_genres
RIGHT JOIN tv_show_genres ON tv_show_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
