select airline_name, flight_num, departure_airport, departure_time, arrival_airport, arrival_time, status
from flight
where flight_num = '{}' and airline_name = '{}' and date_format(arrival_time,'%Y-%m-%d') = '{}'
