# Write your MySQL query statement below
# swap seat id of every 2 consecutive students, if the no. of students is odd, the id of the last student is not swapped

select 
    case 
    when Mod(id, 2) = 0
        then id-1
    when mod(id, 2) != 0 and id  = (select count(*) from seat)
        then id
    Else id+1
    End as id, 
    student
    from seat
    order by id asc;
    