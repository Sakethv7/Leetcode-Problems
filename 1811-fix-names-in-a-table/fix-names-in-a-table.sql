# Write your MySQL query statement below
# first character uppercase and rest are lowercase
#order by user id

 #upper ( left(name, 1)) extracts the first charatcer of the string may also indicate starting point
# lower substring name, 2 extracts 2nd element of the string and ididcates starting point of the substring and converts it to lower
select
    user_id,
    concat( UPPER(left(name, 1)), lower(substring(name,2))) as name
from
    users
order by
    user_id;