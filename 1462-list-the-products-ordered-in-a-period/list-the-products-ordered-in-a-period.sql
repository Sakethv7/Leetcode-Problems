# Write your MySQL query statement below
-- products orders, names of products that have ay least 100 units ordered in feb 2020 and their amount
-- product_name of products who sold at least 100 units ordered in order date  2020-02

select 
    p.product_name, 
    sum(o.unit) as unit
from products p 
join orders o on p.product_id =  o.product_id
where DATE_FORMAT(o.order_date, '%Y-%m') = '2020-02'
group by p.product_name
having sum(o.unit) >= 100;