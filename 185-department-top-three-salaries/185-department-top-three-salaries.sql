# Write your MySQL query statement below

with T1 as 
(select A.*, B.name as dep_name
from Employee A 
left join 
Department B
on A.departmentId = B.id), 

T2 as 
(select T1.*, dense_rank() over (partition by dep_name order by salary DESC) as "den_rank"
from T1)


select T2.dep_name as Department, T2.name as Employee, salary as Salary 
from T2 
where T2.den_rank <= 3