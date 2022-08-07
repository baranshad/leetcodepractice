# Write your MySQL query statement below
with T1 as 
(select A.*, B.name as Departmentname
from Employee A
left join 
Department B
on A.departmentId = B.id)


select distinct Departmentname as Department, name as Employee, salary as Salary
from T1
where (T1.Departmentname, T1.salary) in 
(select Departmentname, max(salary) 
 from T1 group by Departmentname)
