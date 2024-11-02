# Write your MySQL query statement below
# only player 1 as device id is same, player ids connected on consecutive days, in example 1 divide by distinct count(player_id)

#-- CTE to find the first activity date for each player
with first_day as (
    select 
        player_id,
        min(event_date) as first_day
    from activity
    group by player_id
)

#-- Calculate fraction of players with activity on the day after their first activity
select round(
    count(a.player_id)/ (
        select count(distinct b.player_id) from activity b

    ), 2
) as fraction

# -- Join activity with first_day to check consecutive day activity
from activity a 
join first_day using(player_id)
where datediff(a.event_date, first_day.first_day) = 1;