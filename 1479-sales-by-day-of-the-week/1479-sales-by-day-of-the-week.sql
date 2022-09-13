# Write your MySQL query statement below





with T1 as 
(select  A.quantity,  B.item_category, weekday(A.order_date) as weekday
from Orders A 
right join 
Items B
on A.item_id = B.item_id),

T2 as (
select distinct item_category as Category, weekday,
sum(quantity) over(partition by item_category, weekday) as quantities
from T1
order by Category)


select 
category, 
sum(if (weekday = 0, quantities, 0)) as Monday,
sum(if (weekday = 1, quantities, 0)) as Tuesday,
sum(if (weekday = 2, quantities, 0)) as Wednesday,
sum(if (weekday = 3, quantities, 0)) as Thursday,
sum(if (weekday = 4, quantities, 0)) as Friday,
sum(if (weekday = 5, quantities, 0)) as Saturday,
sum(if (weekday = 6, quantities, 0)) as Sunday
from T2
group by category