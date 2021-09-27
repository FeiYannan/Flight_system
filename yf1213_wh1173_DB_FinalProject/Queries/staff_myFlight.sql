select airline_name, flight_num, departure_time, departure_airport, arrival_time, arrival_airport, price, status
from flight
where airline_name = '{}' and  departure_time >= '{}' and departure_time <= '{}'
order by departure_time


-- select airline_name, flight_num, departure_time, departure_airport, arrival_time, arrival_airport, price, status
-- from flight
-- where airline_name = "Eastern" and  departure_time >= "2020-01-01" and departure_time <= "2021-12-31"
-- order by departure_time