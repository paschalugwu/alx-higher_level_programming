-- Lists all Comedy shows in the database
SELECT t.`title`
  FROM `tv_shows` AS t
       -- Join with tv_show_genres table
       INNER JOIN `tv_show_genres` AS s
       ON t.`id` = s.`show_id`
 
       -- Join with tv_genres table
       INNER JOIN `tv_genres` AS g
       ON g.`id` = s.`genre_id`
       -- Filter for Comedy genre
       WHERE g.`name` = "Comedy"
ORDER BY t.`title`;
