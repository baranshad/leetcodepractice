# Write your MySQL query statement below
with T1 as 
(select T.client_id as newid, T.status, T.request_at
 from Trips T 
 left join Users U
 on U.users_id = T.client_id
 left join Users U2 
on T.driver_id = U2.users_id
 where U.banned != "Yes" and U2.banned != "Yes" and T.request_at >= '2013-10-01' and T.request_at <= '2013-10-03' )
 

 
 select 
 request_at as Day, 
 round(sum(case when status like 'can%' then 1 else 0 end) / count(*) , 2) as "Cancellation Rate" 
 from T1
 group by request_at 
 

 
#round(sum(case when t.status like 'can%' then 1 else 0 end) / sum(1), 2) 

