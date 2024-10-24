# Write your MySQL query statement below
#delete alld duplicate emails, keeping only one email with smallest id

delete p2
from person p1 join person p2 
on p1.email = p2.email
and p1.id < p2.id