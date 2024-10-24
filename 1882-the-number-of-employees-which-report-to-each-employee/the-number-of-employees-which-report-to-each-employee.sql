# Write your MySQL query statement below
select 
    e1.employee_id, 
    e1.name,
    count(e2.reports_to) as reports_count,
    Round(Avg(e2.age), 0) as average_age
from
    employees e1 
left join
    employees e2
on 
    e1.employee_id = e2.reports_to
group by
    e1.employee_id, 
    e1.name
having
    reports_count > 0
order by
    e1.employee_id asc,
    reports_count desc,
    average_age desc;