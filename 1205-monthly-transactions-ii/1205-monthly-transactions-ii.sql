# Write your MySQL query statement below
SELECT
    month,
    country,
    count(case when state = 'approved' then 1 else null end) as 'approved_count', 
    IFNULL(sum(case when state = 'approved' then amount else null end), 0) as 'approved_amount',
    count(case when state = 'chargeback' then 1 else null end) as 'chargeback_count', 
    IFNULL(sum(case when state = 'chargeback' then amount else null end), 0) as 'chargeback_amount'
FROM (
    SELECT 
        left(C.trans_date, 7) AS 'month', 
        country, 
        'chargeback' AS state, 
        amount
    FROM Transactions T
    RIGHT JOIN Chargebacks C ON T.id = C.trans_id
    UNION ALL
    SELECT 
        left(trans_date, 7) AS 'month', 
        country, 
        state, 
        amount
    FROM Transactions
    WHERE state = 'approved'
) AS Filtered
GROUP BY month, country