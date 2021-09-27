select ticket_id, purchase_date, airline_name, flight_num, departure_time, departure_airport, arrival_time, arrival_airport, price, status
from ticket natural join flight natural join purchases
where customer_email = '{}' and departure_time >= '{}' and departure_time <= '{}'
order by departure_time asc

 

-- select ticket_id, airline_name, flight_num, departure_time, departure_airport, arrival_time, arrival_airport, price, status
-- from ticket natural join flight natural join purchases
-- where customer_email = 1 and departure_time >= now() and departure_time <= "9999-12-31"
-- order by departure_time asc