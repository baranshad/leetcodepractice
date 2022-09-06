# Write your MySQL query statement below


with T1 as 
(select A.* , B.name as dept_name
from Employee A
left join 
Department B
on A.departmentId = B.id), 

T2 as
(select * , Dense_rank () over(partition by dept_name order by salary DESC) as Den_rank 
from T1 )


select dept_name as Department, name as Employee, salary as Salary
from T2
where Den_rank <=3 
