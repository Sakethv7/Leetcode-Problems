# Write your MySQL query statement below
# report all employees with their primary deparment, employee_id, department_id

SELECT employee_id, department_id
FROM Employee
GROUP BY employee_id
HAVING COUNT(employee_id) = 1

UNION

SELECT employee_id, department_id
FROM Employee
WHERE primary_flag = 'Y';