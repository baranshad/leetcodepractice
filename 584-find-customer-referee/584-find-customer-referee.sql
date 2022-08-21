# Write your MySQL query statement below
select  Customer.name 
from Customer 
where referee_id is Null or referee_id != 2 