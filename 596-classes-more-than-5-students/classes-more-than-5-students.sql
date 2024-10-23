# Write your MySQL query statement below
SELECT class
FROM courses
group by class
having COUNT(DISTINCT student) >= 5;