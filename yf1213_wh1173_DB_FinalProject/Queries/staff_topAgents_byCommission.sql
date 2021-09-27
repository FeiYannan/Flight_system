select * from (select booking_agent_id, email from booking_agent) as b natural join
(select *
from (select booking_agent_id, sum(price)*0.1 as commission from flight natural join  purchases natural join booking_agent natural join (select * from ticket where airline_name = '{}') as mytickets
    where purchase_date >= date_sub('{}', interval '{}' month) and purchase_date <= '{}' group by booking_agent_id order by commission) as t
where 1=1 limit 5
) as s