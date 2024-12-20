# Write your MySQL query statement below
# find the names of salespersons with no orders of company name red

-- select s.name 
-- from orders o 
-- join company c
-- on (o.com_id = c.com_id and c.name = 'Red') # this table joined on orders and company has no other data except for the data that has name as red
-- right join salesperson s # it then right joins on salesperson  
-- on s.sales_id =  o.sales_id
-- where o.sales_id is null


select s.name from Salesperson s 
where s.sales_id not in 
(select o.sales_id from orders o left join company c on o.com_id = c.com_id where c.name = 'RED')