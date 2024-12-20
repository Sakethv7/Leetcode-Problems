select 
    user_id, name, mail
from 
    users
where mail regexp '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\\.com$'
order by
    user_id asc;