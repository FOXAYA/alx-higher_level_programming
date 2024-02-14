-- use left JOIN and subquery
-- Execute: cat 101-not_a_comedy.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
SELECT title 
FROM tv_shows
WHERE title NOT IN (SELECT tv_shows.title
	FROM tv_shows
	LEFT JOIN tv_show_genres
	ON tv_shows.id = tv_show_genres.show_id
	LEFT JOIN tv_genres
	ON tv_show_genres.genre_id = tv_genres.id
	WHERE tv_genres.name = 'Comedy')
ORDER BY 1 ASC;
