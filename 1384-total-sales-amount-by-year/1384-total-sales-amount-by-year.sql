# Write your MySQL query statement below
with recursive cte as
(select 
start_year as report_year 
from (select min(year(period_start)) as start_year, 
        max(year(period_end)) as end_year 
    from sales) a

 
 union all 
 
 select report_year +1 
 from cte, (select min(year(period_start)) as start_year, 
        max(year(period_end)) as end_year 
    from sales) b 
    where report_year < end_year
)


select 

Sales.product_id, 
Product.product_name, 
cast(cte.report_year as char) as report_year, 
(datediff(
case when year(period_end) != cte.report_year 
    then cast(CONCAT(cast(cte.report_year as char), '-12','-31') as date) 
    else period_end
    end, 
    
case when year(period_start) != cte.report_year 
    then cast(concat(cast(cte.report_year as char), '-01', '-01') as date)
    else period_start 
    end
) + 1) * average_daily_sales as total_amount 
from Sales 
left join Product on Sales.product_id = Product.product_id 
left join cte on cte.report_year >= year(period_start) and cte.report_year <= year(period_end)

order by 1,3 asc