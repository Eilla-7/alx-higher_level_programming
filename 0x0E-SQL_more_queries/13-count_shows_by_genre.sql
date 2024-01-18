st genres with the number of shows linked in hbtn_0d_tvshows database
USE `hbtn_0d_tvshows`; -- Replace with the actual database name
SELECT
    tv_genres.name AS genre,
    COUNT(tv_show_genres.show_id) AS number_of_shows
FROM
    tv_genres
LEFT JOIN
    tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY
    genre
ORDER BY
    number_of_shows DESC;
