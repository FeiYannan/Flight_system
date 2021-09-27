select *
from (select customer_email, count(ticket_id) as ticket_number from (select * from purchases where booking_agent_id = '{}') as p natural join ticket natural join flight
    where purchase_date >= date_sub('{}', interval '{}' month) and purchase_date <= '{}' group by customer_email order by ticket_number desc) as t
where 1=1 limit 5


-- select *
-- from (select customer_email, count(ticket_id) as ticket_number from (select * from purchases where booking_agent_id = 1) as p natural join ticket natural join flight
--     where purchase_date >= date_sub("2021-06-01", interval 12 month) and purchase_date <= "2021-06-01" group by customer_email order by ticket_number desc) as t
-- where 1=1 limit 5