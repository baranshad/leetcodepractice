# Write your MySQL query statement below
select distinct A.customer_id 
from 
Customer A 
group by A.customer_id 
having count(distinct product_key) = (select count(distinct product_key) from Product)
 