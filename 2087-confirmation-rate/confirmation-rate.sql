# Write your MySQL query statement below
# 2 tables signups confirmations
# confirmation rate is number of confirmed msgs/total requested confirmation msgs
#confirmation rate = 0 for user who did not request confirmation, rodun 2 to decimal places

# left join

select s.user_id, 
round(avg(if(c.action="confirmed", 1, 0)),2) as confirmation_rate # confirmation rate is basically average (number of confirmed msgs to total actions)
#this ensures if there is no function rounding for a value then it will return 0
from signups s left join confirmations c
on s.user_id = c.user_id
group by s.user_id;