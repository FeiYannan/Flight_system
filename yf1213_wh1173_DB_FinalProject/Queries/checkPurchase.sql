select count(*) as sold, seats 
from ticket natural join airplane natural join flight
where airline_name= '{}' and flight_num= '{}'

