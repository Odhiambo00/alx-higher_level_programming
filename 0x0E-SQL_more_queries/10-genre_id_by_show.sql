-- lists all shows
SELECT show.title, show_gen.genre_id FROM tv_shows AS shows
INNER JOIN tv_show_genres ON shows.id = show_gen.show_id
ORDER BY shows.title, show_gen.genre_id;
