# Write your MySQL query statement below

with T1 as 
(select visited_on, sum(amount) as amount 
from Customer 
group by visited_on 
order by visited_on), 

T2 as (
select distinct visited_on, sum(amount) over (order by visited_on ROWS between 6 preceding and current row) as amount,  round(avg(amount) over (order by visited_on ROWS between 6 preceding and current row), 2) as average_amount, row_number () over (order by visited_on) as row_num
from T1)


select visited_on, amount, average_amount 
from T2 
where T2.row_num >= 7



