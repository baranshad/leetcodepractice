# Write your MySQL query statement below
with T1 
as 
(select *, avg(occurences) over(partition by event_type) as avg_activity
from Events) 

select business_id
from T1
where occurences > avg_activity
group by business_id 
having count(distinct event_type) > 1 

#with allEvents as (select business_id,occurences,
#avg(occurences) over(partition by event_type) as avg_activity from Events) 
#select business_id from allEvents where occurences > avg_activity 
#group by business_id having count(avg_activity) > 1;


 