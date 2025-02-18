# Write your MySQL query statement below

# find the numbers that appear at least 3 times consecutively
# we extract only the number that appears consecutively

select distinct num as ConsecutiveNums 
from
(   
    select num,
        lead(num, 1) over (order by id) as next1, 
        lead(num, 2) over (order by id) as next2 
    from logs
) new_table
where num = next1 and num = next2