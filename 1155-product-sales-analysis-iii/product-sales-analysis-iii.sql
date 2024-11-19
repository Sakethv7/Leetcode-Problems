# Write your MySQL query statement below
#product_id, first year, quantity, price for the first year of every product  sold
# 2 tables Sales, Product


#create a CTE to include a window function and assign a rank to each record based on the year of sale
with sales2 as 
(select *, rank() over (partition by product_id order by year) as row_rank
from sales)

select product_id, year as first_year,quantity, price from sales2
where row_rank = 1;

