select ticket_id, purchase_date, flight_num, departure_time, departure_airport, arrival_time, arrival_airport, price, status
from (select * from ticket where airline_name = '{}') as t 
    natural join (select * from flight where airline_name = '{}') as f
    natural join (select * from purchases where customer_email = '{}') as p
