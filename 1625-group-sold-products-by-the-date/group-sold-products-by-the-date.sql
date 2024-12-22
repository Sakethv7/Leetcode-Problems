# Write your MySQL query statement below
# write a solution to find for each date the number of different productss sold and their names 
# order by sell_date
select sell_date, count( Distinct product) as num_sold, 
group_concat( Distinct product order by product asc separator ',') as products
from Activities
group by sell_date order by sell_date asc
