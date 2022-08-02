# Write your MySQL query statement below
select distinct 
l1.num as ConsecutiveNums
from 
logs l1 
inner join 
logs l2 on l1.id = l2.id-1 and l1.num = l2.num 
inner join 
logs l3 on l3.id = l1.id+2 and l1.num = l3.num
