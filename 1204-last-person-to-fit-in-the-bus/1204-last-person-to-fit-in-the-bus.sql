# Write your MySQL query statement below
select person_name 
from 
(select person_name, sum(weight) over(order by turn) as Total
from Queue
order by turn) A 
where A.Total <= 1000
order by Total DESC 
limit 1 


 
