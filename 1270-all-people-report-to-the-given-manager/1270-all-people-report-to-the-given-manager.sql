# Write your MySQL query statement below
with recursive T1 as 
(select employee_id 
from Employees 
 where employee_id != 1 and manager_id = 1 
union 
select A.employee_id 
from employees A 
inner join 
T1 B 
on B.employee_id = A.manager_id ) 

select * from T1