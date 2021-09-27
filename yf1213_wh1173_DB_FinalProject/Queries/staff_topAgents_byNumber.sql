select * from (select booking_agent_id, email from booking_agent) as b natural join
(select *
from (select booking_agent_id, count(ticket_id) as ticket_number from flight natural join  purchases natural join booking_agent natural join (select * from ticket where airline_name = '{}') as mytickets
    where purchase_date >= date_sub('{}', interval '{}' month) and purchase_date <= '{}' group by booking_agent_id order by ticket_number) as t
where 1=1 limit 5
) as s


-- select * from (select booking_agent_id, email from booking_agent) as b natural join
-- (select *
-- from (select booking_agent_id, count(ticket_id) as ticket_number from flight natural join  purchases natural join booking_agent natural join (select * from ticket where airline_name = "Eastern") as mytickets
--     where purchase_date >= date_sub("2021-06-06", interval 12 month) and purchase_date <= "2021-06-06" group by booking_agent_id order by ticket_number) as t
-- where 1=1 limit 5
-- ) as s