# Write your MySQL query statement below
with T1 
as 
(select 
count(distinct B.post_id)/count(distinct A.post_id) as fractionbyday
from Actions A
left join 
Removals B
on A.post_id = B.post_id
where A.extra = "spam"
group by action_date)

select round(avg(fractionbyday)*100, 2) as average_daily_percent
from T1



