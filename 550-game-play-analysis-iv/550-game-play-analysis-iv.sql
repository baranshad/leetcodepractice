# Write your MySQL query statement below

WITH temp AS (
SELECT a1.player_id AS 'good_player', MIN(a1.event_date) AS 'first_login'
FROM Activity a1
GROUP BY a1.player_id
),

temp2 AS (
SELECT a2.player_id, a2.event_date, a3.event_date AS 'next_day'
FROM Activity a2, Activity a3
WHERE a2.player_id = a3.player_id AND a3.event_date = a2.event_date + 1
)


SELECT ROUND(COUNT(player_id)/(SELECT COUNT(DISTINCT player_id) FROM Activity),2) AS 'fraction'
FROM temp2
LEFT JOIN temp
ON temp.good_player = temp2.player_id AND temp.first_login = temp2.event_date
WHERE temp.first_login IS NOT NULL