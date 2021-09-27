select airline_name, flight_num, departure_airport, departure_time, arrival_airport, arrival_time, status
from flight
where flight_num = '{}' and airline_name = '{}' and date_format(departure_time,'%Y-%m-%d') = '{}'




-- select status, flight_num, airline_name, departure_time, arrival_time, departure_airport, arrival_airport
-- from flight
-- where flight_num = 1 and airline_name = "Eastern" and date_format(departure_time,'%Y-%m-%d') = "2021-05-11"