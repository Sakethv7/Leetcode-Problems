# Write your MySQL query statement below
select Max(num) as num 
from (
        select num 
        from mynumbers
        group by num
        having count(*) = 1
) as singlenumbers