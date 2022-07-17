# Write your MySQL query statement below
select B.dept_name, count(distinct A.student_id) as student_number 
from student A 
right join department B
on A.dept_id = B.dept_id 
group by B.dept_id 
order by student_number DESC, B.dept_name; 