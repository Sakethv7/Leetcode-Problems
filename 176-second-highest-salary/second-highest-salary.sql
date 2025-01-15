# Write your MySQL query statement below
select max(salary) as SecondHighestSalary
from Employee 
where salary not in (select Max(salary) from employee)