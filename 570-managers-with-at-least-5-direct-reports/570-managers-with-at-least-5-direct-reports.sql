# Write your MySQL query statement below

select A.name 
from Employee A 
left join 
Employee B 
on A.id = B.managerId 
where B.managerId is not Null 
group by B.managerId 
having count(distinct B.id) >= 5 ;