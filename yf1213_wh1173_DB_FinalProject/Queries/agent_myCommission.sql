select sum(price)*0.1 as total_commission, count(*) as number, sum(price)*0.1/count(*) as average
from ticket natural join flight natural join (select * from purchases where booking_agent_id = '{}') as p 
where purchase_date >= date_sub('{}', interval '{}' month) and purchase_date <= '{}';


-- select sum(price)*0.1 as total_commision, count(*) as number, sum(price)*0.1/count(*) as average
-- from ticket natural join flight natural join purchases
-- where booking_agent_id = 1 and purchase_date >= "2021-01-01" and purchase_date <= "2021-12-31";

