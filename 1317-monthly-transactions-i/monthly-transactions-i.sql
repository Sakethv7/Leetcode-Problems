# Write your MySQL query statement below
#no. of transactions and their total amount of approved transactions and their total amount
#  month, country

select DATE_FORMAT(trans_date, '%Y-%m') as month, 
        country, count(id) as trans_count, 
        Sum(case when state = 'approved' then 1 else 0 end) as approved_count,
        Sum(amount) as trans_total_amount, 
        Sum(case when state = 'approved' then amount else 0 end) as approved_total_amount
from transactions
group by month, country
order by month, country;



