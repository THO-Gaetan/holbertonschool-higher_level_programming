-- lists all genre from hbtn_0d_tvshows
-- display the number of shows linked
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id)
AS number_of_shows
From tv_genres
INNER JOIN tv_show.genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.id
ORDER BY number_of_shows DESC;
