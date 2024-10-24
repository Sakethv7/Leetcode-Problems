# Write your MySQL query statement below
#sum of 2 sides of a triangle must be greater than the third side

select 
    x, y, z,
    Case
        when x+y >z and x+z > y and y+z > x then 'Yes'
        else 'No'
    End as triangle
from 
    Triangle;
