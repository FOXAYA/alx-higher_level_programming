-- Function SUM
-- Execute: cat 102-rating_shows.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows_rate
SELECT
tv_shows.title, SUM(tv_show_ratings.rate) AS rating
FROM tv_shows
LEFT JOIN tv_show_ratings
ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.title
ORDER BY 2 DESC;
