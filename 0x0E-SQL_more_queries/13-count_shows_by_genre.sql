-- Counts number of shows linked to each tv show
SELECT tv_genres.name, COUNT(*) as number_of_shows
FROM tv_genres
     INNER JOIN tv_show_genres
     ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
