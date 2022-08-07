# Write your MySQL query statement below

select distinct 
A.email as Email 
from Person A 
inner join 
Person B 
on A.email = B.email and A.id != B.id