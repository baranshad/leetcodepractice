# Write your MySQL query statement below
select 
 A.name as Customers 
from Customers A
where A.id not in (select customerId from Orders); 