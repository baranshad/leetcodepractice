# Write your MySQL query statement below
With Customer_Total
AS
(
Select customer_id, count(distinct Customer.product_key) as Customer_Count
FROM Customer
GROUP BY Customer_id
),

Product_Total
AS
(
Select count(product_key) as Product_Count
FROM Product
)

Select customer_id
FROM Customer_Total
WHERE Customer_Count in (Select Product_Count FROM Product_total)