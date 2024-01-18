-- Lists all genres not linked to the show Dexter
-- Retrieve distinct genres linked to the show Dexter
SELECT DISTINCT `name`
  FROM `tv_genres` AS g
       INNER JOIN `tv_show_genres` AS s
       ON g.`id` = s.`genre_id`

       INNER JOIN `tv_shows` AS t
       ON s.`show_id` = t.`id`
       WHERE t.`title` = "Dexter";

-- Retrieve all distinct genres
SELECT DISTINCT `name`
  FROM `tv_genres`
  WHERE `name` NOT IN
        -- Exclude genres linked to the show Dexter
        (SELECT DISTINCT `name`
           FROM `tv_genres` AS g
                INNER JOIN `tv_show_genres` AS s
                ON g.`id` = s.`genre_id`
    
                INNER JOIN `tv_shows` AS t
                ON s.`show_id` = t.`id`
                WHERE t.`title` = "Dexter")
ORDER BY g.`name`;
