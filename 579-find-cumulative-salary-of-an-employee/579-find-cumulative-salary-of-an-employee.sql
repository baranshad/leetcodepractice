# Write your MySQL query statement below

with T1 as 
(select *, sum(salary) over (partition by id order by month 
                            range between 2 preceding and current row)as sumofsalary
from Employee)

select C.id,
C.month, C.sumofsalary as Salary 
from 
(select * , rank() over (partition by T1.id order by T1.month DESC) as "ranknew"
 from T1
order by id ASC, month DESC
) C 
where C.ranknew >1

