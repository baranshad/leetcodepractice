# Write your MySQL query statement below
select distinct 
A.num as ConsecutiveNums
from Logs A
inner join 
Logs B 
on A.num = B.num and  A.id + 1 = B.id  
inner join 
Logs C 
on A.num = C.num and A.id + 2 = C.id 