# Write your MySQL query statement below
with T1 as 
(select A.*, B.name as deapartmentname
from Employee A 
left join 
Department B
on A.departmentId = B.id)


select T2.deapartmentname as Department, T2.name as Employee, T2.Salary
from 
(select *, 
dense_rank() over(partition by  deapartmentname order by Salary DESC) as 'rank'
from T1) as T2 
where T2.rank <=3 
#group by deapartmentname
