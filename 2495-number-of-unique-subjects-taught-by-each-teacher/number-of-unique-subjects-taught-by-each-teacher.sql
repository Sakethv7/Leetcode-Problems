# Write your MySQL query statement below
# calculate the number of unique (distinct) subjects each teacher teasches in the university
#teach_id, subject_id, dept_id

Select teacher_id,  count( distinct(subject_id)) as cnt
from teacher
group by teacher_id