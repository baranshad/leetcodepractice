# Write your MySQL query statement below
WITH cte AS(SELECT id, MAX(month) AS month FROM Employee GROUP BY id)

SELECT id, month, SUM(salary) OVER(PARTITION BY id ORDER BY month RANGE BETWEEN 2 PRECEDING AND CURRENT ROW) AS salary
FROM Employee
WHERE NOT EXISTS (SELECT id, month FROM cte WHERE Employee.id=cte.id AND Employee.month=cte.month )
ORDER BY id, month DESC;