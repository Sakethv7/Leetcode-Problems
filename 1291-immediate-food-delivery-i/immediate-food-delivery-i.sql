# Write your MySQL query statement below
#if del date = order date then it is immediate, else scheduled
#return percentage of immediate orders

WITH immediate AS (
    SELECT delivery_id, customer_id, order_date, customer_pref_delivery_date
    FROM Delivery
    WHERE order_date = customer_pref_delivery_date
)
SELECT ROUND((COUNT(immediate.delivery_id) * 1.0 / COUNT(delivery.delivery_id)) * 100, 2) AS immediate_percentage -- Main query to calculate the percentage of immediate deliveries
FROM Delivery -- Calculate percentage and round to 2 decimal places
LEFT JOIN immediate ON Delivery.delivery_id = immediate.delivery_id; -- Left join to include all deliveries