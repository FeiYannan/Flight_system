select sum(price) 
from purchases natural join ticket natural join flight
where airline_name = '{}' and booking_agent_id is null 
and purchase_date >= date_sub('{}', interval '{}' month) and purchase_date <= '{}'