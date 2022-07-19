# Write your MySQL query statement below
with T1 as 
(select *, (case when host_goals > guest_goals then 3 
when host_goals = guest_goals then 1 else 0 end) as hostpoint, 

 (case when host_goals < guest_goals then 3 
 when host_goals = guest_goals then 1 
 else 0 end ) as guestpoint
 from Matches), 
 
 T2 as 
 (select host_team as team_id, hostpoint as num_points1 
 from T1 
 union all 
 select guest_team as team_id, guestpoint as num_points1
 from T1)
 
 select distinct C.team_id, C.team_name, sum(ifnull(T2.num_points1, 0)) as num_points
 from Teams C
 left join 
 T2 
 on C.team_id = T2.team_id 
group by C.team_id
order by num_points DESC, team_id

#select distinct C.team_id, team_name, sum(ifnull(B.num_points1, 0)) as num_points 
#from Teams C 
#left join 
#(select host_team as team_id, hostpoint as num_points1
#from totalpoint A 
#union all
#select guest_team as team_id, guestpoint as num_points1
#from totalpoint A) B 
#on C.team_id = B.team_id
#group by C.team_id 
#order by num_points DESC, team_id
