select * from 
(select customer_email, count(distinct ticket_id) as number_of_tickets
    from customer natural join purchases natural join (select * from ticket where airline_name = '{}') as mytickets
    where purchase_date >= date_sub('{}', interval '{}' month) and purchase_date <= '{}' group by customer_email order by number_of_tickets) as t
where 1=1 limit 5
