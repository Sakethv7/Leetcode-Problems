# Write your MySQL query statement below
# find avg selling price for each product  as average_price rounded to 2 decimal places Round(average_price, 2)
# if product does not have any sold units, average_price = 0
# print product_id and average_price
# units * price per product_id = total price of product / number of products sold = no.of units sold 

select p.product_id, 
   COALESCE(ROUND(SUM(p.price * u.units) / SUM(u.units), 2), 0) AS average_price
from prices p left join unitssold u
on p.product_id = u.product_id
and 
    u.purchase_date between p.start_date and p.end_date
group by 
    p.product_id;