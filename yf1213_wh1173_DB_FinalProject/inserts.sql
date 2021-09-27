INSERT INTO `airline` (`airline_name`) VALUES
('Eastern'),
('Southern'),
('Western');



INSERT INTO `airplane` (`airline_name`, `airplane_id`, `seats`) VALUES
('Eastern', 737001, 100),
('Eastern', 737002, 100),
('Eastern', 747003, 200),
('Southern', 747001, 200),
('Southern', 747002, 200),
('Western', 320001, 150),
('Western', 320002, 150),
('Western', 737003, 150);



INSERT INTO `airport` (`airport_name`, `airport_city`) VALUES
('Daxing', 'Beijing'),
('Hongqiao', 'Shanghai'),
('Pudong', 'Shanghai'),
('Taoxian', 'Shenyang'),
('Shoudu', 'Beijing'),
('Liuting', 'Qingdao');



INSERT INTO `booking_agent` (`email`, `password`, `booking_agent_id`) VALUES
('xiecheng@xiecheng.com', 'xiecheng', 1),
('feizhu@feizhu.com', 'feizhu', 2),
('agent3@agent3.com', 'agent3', 3),
('agent4@agent4.com', 'agent4', 4),
('agent5@agent5.com', 'agent5', 5),
('agent6@agent6.com', 'agent6', 6),
('agent7@agent7.com', 'agent7', 7),
('agent8@agent8.com', 'agent8', 8);



INSERT INTO `customer` (`email`, `name`, `password`, `building_number`, `street`, `city`, `state`, `phone_number`, `passport_number`, `passport_expiration`, `passport_country`, `date_of_birth`) VALUES
('user1@user1.com', 'user1', 'user1', '1', '1', '1', '1', 1, '1', '2021-05-07', '1', '2021-05-03'),
('user2@user2.com', 'user2', 'user2', '2', '2', '2', '2', 2, '2', '2021-05-04', '2', '2021-05-03'),
('user3@user3.com', 'user3', 'user3', '3', '3', '3', '3', 3, '3', '2021-05-10', '3', '2021-05-19'),
('user1@user4.com', 'user4', 'user4', '1', '1', '1', '1', 1, '1', '2021-05-07', '1', '2021-05-03'),
('user1@user5.com', 'user5', 'user5', '1', '1', '1', '1', 1, '1', '2021-05-07', '1', '2021-05-03'),
('user1@user6.com', 'user6', 'user6', '1', '1', '1', '1', 1, '1', '2021-05-07', '1', '2021-05-03'),
('user1@user7.com', 'user7', 'user7', '1', '1', '1', '1', 1, '1', '2021-05-07', '1', '2021-05-03');




INSERT INTO `flight` (`airline_name`, `flight_num`, `departure_airport`, `departure_time`, `arrival_airport`, `arrival_time`, `price`, `status`, `airplane_id`) VALUES
('Eastern', 1, 'Daxing', '2021-05-11 15:49:05', 'Pudong', '2021-05-11 17:49:05', '1000', 'upcoming', 737001),
('Eastern', 2, 'Shoudu', '2021-06-11 16:00:05', 'Pudong', '2021-06-11 18:00:05', '1500', 'upcoming', 737001),
('Eastern', 3, 'Taoxian', '2021-05-20 13:00:05', 'Liuting', '2021-05-20 15:00:05', '1500', 'upcoming', 737001),
('Southern', 2, 'Taoxian', '2021-05-04 15:51:53', 'Hongqiao', '2021-05-04 17:51:53', '2000', 'upcoming', 747001);



-- insert into ticket (airline_name, flight_num) values("Eastern", 1);
-- insert into purchases(ticket_id, customer_email, purchase_date) values
-- ((select max(ticket_id) from ticket), 1, curdate());

-- insert into ticket (airline_name, flight_num)
-- values("Southern", 2);
-- insert into purchases(ticket_id, customer_email, purchase_date)
-- values((select max(ticket_id) from ticket), 2, curdate());



-- insert into ticket (airline_name, flight_num)
-- values("Eastern", 1);

-- insert into purchases(ticket_id, customer_email, booking_agent_id, purchase_date)
-- values((select max(ticket_id) from ticket), 1, 1, curdate());
