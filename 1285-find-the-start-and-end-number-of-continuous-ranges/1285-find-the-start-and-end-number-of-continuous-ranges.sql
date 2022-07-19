# Write your MySQL query statement below
with T1 as 
(select log_id,
row_number() over(order by log_id) as diff
from Logs )

select min(log_id) as start_id, max(log_id) as end_id from T1 
group by log_id - diff




#select 
#min(log_id) as start_id, max(log_id) as end_id
#from 
#(select log_id, 
# row_number() over(order by log_id) as diff
#from Logs) A 
#group by log_id - diff
