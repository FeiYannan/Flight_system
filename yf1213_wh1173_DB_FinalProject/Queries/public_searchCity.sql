select airline_name, flight_num,departure_airport, departure_time, arrival_airport, arrival_time ,  status, price
from flight
where departure_airport in (select airport_name from airport where airport_city = '{}') and arrival_airport in (select airport_name from airport where airport_city = '{}') and date_format(departure_time,'%Y-%m-%d') = str_to_date('{}','%Y-%m-%d')


-- select airline_name, flight_num, departure_time, arrival_time, departure_airport, arrival_airport, price, status, airplane_id
-- from flight
-- where departure_airport in (select airport_name from airport where airport_city = "Beijing") and arrival_airport in (select airport_name from airport where airport_city = "Shanghai") and date_format(departure_time,'%Y-%m-%d') = str_to_date("2021-05-11",'%Y-%m-%d')