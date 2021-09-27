select *
from (select airport_city, sum(ticket_number) as total_number from airport natural join
        (select airport_name, count(distinct ticket_id) as ticket_number
        from (select * from ticket where airline_name = '{}') as t natural join purchases natural join airport join (select * from flight where airline_name = '{}') as f on arrival_airport = airport_name
        where purchase_date >= date_sub('{}', interval '{}' month) and purchase_date <= '{}'
        group by airport_name
        ) as s
    group by airport_city
    order by total_number desc
    ) as topCities
where 1=1 limit 3




-- select *
-- from (select airport_city, sum(ticket_number) as total_number from airport natural join
--         (select airport_name, count(distinct ticket_id) as ticket_number
--         from (select * from ticket where airline_name = "Eastern") as t natural join purchases natural join airport join (select * from flight where airline_name = "Eastern") as f on arrival_airport = airport_name
--         where purchase_date >= date_sub("2021-12-31", interval 12 month) and purchase_date <= "2021-12-31"
--         group by airport_name
--         ) as s
--     group by airport_city
--     order by total_number desc
--     ) as topCities
-- where 1=1 limit 3