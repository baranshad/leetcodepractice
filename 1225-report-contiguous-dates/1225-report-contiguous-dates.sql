# Write your MySQL query statement below
with fulltable as 
(select fail_date as dt, 'failed' as status
from Failed
where fail_date >= "2019-01-01" and fail_date <= "2019-12-31"

union 

select success_date as dt, 'succeeded' as status
from Succeeded 
where success_date >= "2019-01-01" and success_date <= "2019-12-31"

order by dt),

segments as 
(select dt, status, row_number() over (order by dt) as row1, 
 row_number() over (partition by status order by dt) as row2,
(row_number() over (order by dt) - row_number() over (partition by status order by dt)) as seg
from fulltable)

select status as period_state,
min(dt) as start_date, max(dt) as end_date 
from segments
group by status, seg 
order by start_date 