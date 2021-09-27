files in "/Queries"
--------supporting_queries---------
--checkPurchase:
    check whether the seats for a flight is sold out

--------public---------
--public_searchAirport:
    searching flights based on departure, arrival AIRPORT and date
--public_searchCity:
    searching flights based on departure, arrival CITY and date
--public_searchStatus_byArrDate:
    searching the status of a specific flight based on flight_number, airline_name and arrival_date
--public_searchStatus_byDepDate:
    searching the status of a specific flight based on flight_number, airline_name and departure_date



-------customer--------
--cus_myFlight:
    search for the flights the current customer has bought
--customer_mySpending:
    search for spending of the current customer
--customer_purchase:
    buy a ticket for the current customer



--------agent---------
--agent_myCommission:
    search for commission of the current agent
--agent_myFlight:
    search for flights that this agent has bought
--agent_purchase:
    buy a ticket throught the current agent
--agent_topCustomers_byCommision:
    search for current agent's top customers by commission
--agent_topCustomers_byNumber:
    search for current agent's top customers by number of tickets they bought


---------staff--------
--staff_Airplane:
    add an airplane for the airline this staff belongs to
--staff_addAirport:
    add an airport for the airline this staff belongs to
--staff_allCustomerForFlight
    search for all customers for a certain flight
--staff_changeStatus:
    change the status of a flight belongs to this airline
--staff_createNewFlight:
    create a new flight for this airline
--flightForCustomer:
    search for all flights of this airline that a customer has bought
--staff_myFlight:
    search for all flights of this airline
--staff_reports:
    search for number of tickets the airline sells by month
--staff_revenueAgent:
    search for total income (tickets sold through agent)
--staff_revenueCustomer:
    search for total income (tickets sold through customer)
--staff_topAgents_byCommision:
    search for top agents by commission
--staff_topAgents_byNumber:
    search for top agents by Number of tickets sold
--staff_topDestination:
    search for top destinations for this airline


