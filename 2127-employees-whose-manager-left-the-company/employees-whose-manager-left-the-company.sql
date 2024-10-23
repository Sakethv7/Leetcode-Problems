#id's whose salayary < 30000 and manager left the company- manager leaves, info deleted from employees table
#return ordered by employee id

select employee_id from employees
where salary < '30000' and
manager_id not in (select employee_id from employees)
order by employee_id;