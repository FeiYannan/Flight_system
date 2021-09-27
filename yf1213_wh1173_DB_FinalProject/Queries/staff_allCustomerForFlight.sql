select customer_email, name, phone_number, passport_number, count(ticket_id) as number_of_tickets
from customer join purchases on email = customer_email natural join ticket
where airline_name = '{}' and flight_num = '{}'
group by email


-- select customer_email, name, phone_number, count(ticket_id) as number_of_tickets
-- from customer join purchases on email = customer_email natural join ticket
-- where airline_name = 'Eastern' and flight_num = 1
-- group by email