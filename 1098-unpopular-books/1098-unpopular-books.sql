# Write your MySQL query statement below
with T1 
as (select * 
   from Books 
   where available_from < date_sub('2019-06-23' , interval 1 month)), 
   
 T2 
 as (select *, sum(quantity) as total 
    from Orders
    where dispatch_date between '2018-06-23' and '2019-06-23'
    group by book_id)


select T1.book_id, T1.name 
from T1 
left join T2 
on T1.book_id = T2.book_id
where T2.total <10 or T2.total is null

