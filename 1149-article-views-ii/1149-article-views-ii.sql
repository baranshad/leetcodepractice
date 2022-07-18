# Write your MySQL query statement below
select distinct viewer_id as id 
 from Views A
 group by view_date, viewer_id 
 having count(distinct article_id) > 1
 order by id 

