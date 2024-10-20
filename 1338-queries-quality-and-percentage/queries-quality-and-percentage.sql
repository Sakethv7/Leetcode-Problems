# Write your MySQL query statement below
# query_name, quality = avg of the ratio between every rating and its position and poor_quality percentage = % of all queries with rating less than three. rounded to 2 decimal places

#Avg(sum(rating/position)) - quality
#  (if ((rating<3),0)/count(rating))*100

#group by query_name

Select query_name,
    Round(Avg(rating/position),2) as quality,
    Round(Sum(Case When rating<3 then 1 else 0 END)*100/count(*), 2) as poor_query_percentage
from queries
Where query_name is not Null
group by query_name;