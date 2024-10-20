# Write your MySQL query statement below
# users, register
# % of users registered in each contest rounded to 2 decimals
# result table in descending order of percentage and contest_id in ascending order

#group by contest_id
#left join, percentage = count(distinct of users in that contest)/ total users from users *100

SELECT r.contest_id,
       ROUND(COUNT(DISTINCT r.user_id) * 100.0 / (SELECT COUNT(*) FROM users), 2) AS percentage
FROM register r
GROUP BY r.contest_id
ORDER BY percentage DESC, r.contest_id ASC;
