insert into ticket (airline_name, flight_num)
values('{}', '{}');

insert into purchases(ticket_id, customer_email, booking_agent_id, purchase_date)
values((select max(ticket_id) from ticket), '{}', curdate());