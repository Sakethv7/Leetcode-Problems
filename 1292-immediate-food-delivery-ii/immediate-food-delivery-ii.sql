# Write your MySQL query statement below
# Order immedidate means deliery date= order date, otherwise scheduled
# first order of a customer is the earliest order date
# show percentage of immediate orders in the first orders of all customers rounded to 2 decimal places
# subqueries

SELECT 
    ROUND(SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS immediate_percentage
FROM 
    (SELECT customer_id, 
            order_date, 
            customer_pref_delivery_date
     FROM delivery
     WHERE (customer_id, order_date) IN 
           (SELECT customer_id, MIN(order_date) 
            FROM delivery 
            GROUP BY customer_id)) AS first_orders;