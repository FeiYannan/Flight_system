select sum(price), purchase_month
from ticket natural join flight natural join (select ticket_id, customer_email, purchase_date, date_format(purchase_date,'%Y-%m') as purchase_month from purchases) as t
where customer_email = '{}' and purchase_date >= date_format('{}','%Y-%m-%d')
and purchase_date <= date_format('{}','%Y-%m-%d')
group by purchase_month
order by purchase_month asc


-- select sum(price), purchase_month
-- from ticket natural join flight natural join (select ticket_id, customer_email, purchase_date, date_format(purchase_date,'%Y-%m') as purchase_month from purchases) as t
-- where customer_email = 1 and purchase_date >= date_format("2021-01-01",'%Y-%m-%d')
-- and purchase_date <= date_format("2021-12-31",'%Y-%m-%d')
-- group by purchase_month
-- order by purchase_month desc
