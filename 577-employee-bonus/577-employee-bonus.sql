# Write your MySQL query statement below
select A.name as name, B.bonus as bonus 
from Employee A 
left join 
Bonus B 
on A.empId = B.empId 
where bonus is Null or bonus < 1000;