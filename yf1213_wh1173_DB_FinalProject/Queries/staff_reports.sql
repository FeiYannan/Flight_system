select count(ticket_id), purchase_month
from (select * from ticket where airline_name = '{}') as t
natural join flight 
natural join (select ticket_id, customer_email, purchase_date, date_format(purchase_date,'%Y-%m') as purchase_month from purchases) as p
where purchase_date >= date_format('{}','%Y-%m-%d') and purchase_date <= date_format('{}','%Y-%m-%d')
group by purchase_month
order by purchase_month desc