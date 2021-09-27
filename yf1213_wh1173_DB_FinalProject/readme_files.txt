Databases, 2021 Spring, Final Project
Team: 1. Yannan Fei: Back-end, "init.py" and "/Queries"
      2. Molly He: Front-end, "/static" and "/templates"

Chrome recommended




-----------------------------------------------------------------------------------------
--init.py
  THE FILE USED TO START THE SERVER
  please use "python init.py" to start

  all HTTP requests are written in this file




-----------------------------------------------------------------------------------------
supporting files:
--create.sql
  queries used for creating tables
  please use THIS provided create file because we made some changes

--inserts.sql
  some test data, with users and bought tickets




--------------------------------------------------------------------------------------------------
files in "/Queries"
queries used for cases, see "readme_queries"




-----------------------------------------------------------------------------------------

files in "/templates"

------------------------public-------------------------
--public.html
  This is the starting page of the application. One can either choose to search
  for flight, or click on login to login to be redirect to the login.html.
  Page to search for a flight, based on 3 modes: 1)Departure city, arrival city,
  and date. 2)Departure airport, arrival airport, and date. 3)Flight number,
  airline name, and departure/arrival date (This is for searching flight status).

--purchase.html
  After clicking search on the public.html, user is redirect to this page where
  the searched flight's information is displayed. The user can click on the
  purchase button to purchase. If he/she is not logged in, he/she will be redirected
  to the login page. If he/she is a customer or a agent, a line saying purchase
  success will be displayed, and the database is updated.

--status.html
  Page showing the flight status, including Airline,	Flight number,	Departure
  airport,	Departure time,	Arrival airport,	Arrival time, and	Status.

--login.html
  Page to login through 3 modes: customer, agent or staff. Will display error if
  not match the database entries. If success, then will be redirected to home.html.

--register.html
  Page to register through 3 modes: customer, agent or staff.Will display error if
  there is duplicate in the database entries. If success, then will be redirected
   to login.html.

--home.html
  Page displayed one a user is logged in. The top is a welcome message for the
  user. The left side navigation bar changes based on the type of user. When
  clicking on any of the options in the bar, the right side of the page will
  display the redirected page through iframe. One can choose to log out any time
   they want by clicking on the top right button.


-----------------------customer------------------------
--flight.html
  Page to view all the flights the customer has purchased. He/She can select
  date to specify the range of dates.

--spending.html
  Page to view my spending based on selected dates. The data is displayed in a
  bar chart, with each bar representing the month's money spent.


--------agent---------
--flight_a.html
  Page to view all the flights the agent has purchased. He/She can select
  date to specify the range of dates.

--commission.html
  Page to view commission through selected range of dates. The form will display
  total amount of commission, average commission and total number of tickets sold.

--top_customer.html
  Page to view top 5 customers in past 6 months by number of tickets and by
  commission through bar chart.


-------------------------staff------------------------
--flight_s.html
  Page to view flights operated by the airline the staff works for.
  After sorting by date, staff can click on the view all to see all customers
  flying the flight, by redirecting to detail.html.

--detail.html
  Page providing the customers' email, name, phone number, passport number
  and number of tickets bought.

--add.html
  Page to create new flights/change status of flights/add airplane/add new airport.

--top_agents.html
  Page to see top 5 booking agents by 3 modes: number of tickets bought in the
  past month, number of tickets bought in the past year, and commission received
  last year.

--frequent_customer.html
  Page to see top 5 frequent customers in the last year. Staff can click on the
  view all to see all flights the customer taken on the particular airline, by
  being redirected to customer.html.

--customer.html
  Page to show all flight information of a specific customer, including Ticket ID,
  	Purchase date,	Flight number,	Departure time,	Departure airport,	Arrival
    time,	Arrival airport,	Price (RMB), and	Status.


--report.html
  Page to see total number of tickets sold in a bar chart. Staff can select dates
  to see results on that range of dates.

--revenue.html
  Page to see revenue earned in pie chart comparing the revenue from direct sales
  and indirect sales. The 2 modes are in the last month and last year.

--top_destination.html
  Page to see top 3 most popular destinations for last 3 months and last year.





--------------------------------------------------------------------------------------------------

files in "/static"

-1.jpeg
  The background image for home.html

-foler styles
  Stylesheets linking to the corresponding html.

-folder js
  Scripts linking to the corresponding html.




