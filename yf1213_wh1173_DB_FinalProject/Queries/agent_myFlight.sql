select ticket_id, customer_email, purchase_date, airline_name, flight_num, departure_time, departure_airport, arrival_time, arrival_airport, price, status
from ticket natural join flight natural join purchases
where booking_agent_id = '{}' and  departure_time >= '{}' and departure_time <= '{}'
order by departure_time



-- select ticket_id, customer_email, purchase_date, airline_name, flight_num, departure_time, departure_airport, arrival_time, arrival_airport, price, status
-- from ticket natural join flight natural join purchases
-- where booking_agent_id = 1 and  departure_time >= now() and departure_time <= "9999-12-31"
-- order by departure_time desc
