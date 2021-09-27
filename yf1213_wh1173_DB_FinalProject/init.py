from flask import Flask, render_template, request, session, url_for, redirect, flash
# from flask_login import login_required
import mysql.connector
import time
import datetime 

#Initialize the app from Flask
app = Flask(__name__)

#Configure MySQL
conn = mysql.connector.connect(host='localhost',
					port='8889',
					user='root',
					password='root',
					database='Air')


@app.route('/')
def hello():
 return render_template('public.html')

@app.route('/public')
def public():
 return render_template('public.html')

#Define route for login
@app.route('/login')
def login():
 return render_template('login.html')

@app.route('/flight')
def flight():
 return render_template('flight.html')

@app.route('/flight_a')
def flight_a():
 return render_template('flight_a.html')

@app.route('/flight_s')
def flight_s():
 return render_template('flight_s.html')

@app.route('/purchase')
def purchase():
 return render_template('purchase.html')

@app.route('/spending')
def spending():
 return render_template('spending.html')

@app.route('/commission')
def commission():
 return render_template('commission.html')

@app.route('/top_customer')
def top_customer():
 return render_template('top_customer.html')

@app.route('/add')
def add():
 return render_template('add.html')

@app.route('/top_agents')
def top_agents():
 return render_template('top_agents.html')

@app.route('/frequent_customer')
def frequent_customer():
 return render_template('frequent_customer.html')

@app.route('/report')
def report():
 return render_template('report.html')

@app.route('/revenue')
def revenue():
 return render_template('revenue.html')

@app.route('/top_destinations')
def top_destinations():
 return render_template('top_destinations.html')


#Define route for register
@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/home')
def home():
	username = session['username']
	cursor = conn.cursor()
	query = "SELECT ts, blog_post FROM blog WHERE username = \'{}\' ORDER BY ts DESC"
	cursor.execute(query.format(username))
	data1 = cursor.fetchall()
	cursor.close()
	return render_template('home.html', username=username, posts=data1)


@app.route('/logout')
def logout():
	session.pop('username')
	return redirect('/')




# def login_required(func):
# 	return Inner(func)

# def Inner(func):
# 	try:
# 		s = session['username']
# 		return func()
# 	except:
# 		return render_template('login.html')



#----------------------register------------------------------------------

@app.route('/cus_registerAuth', methods=['GET', 'POST'])
def cus_registerAuth():
	email = request.form['c_email']
	name = request.form['c_name']
	password = request.form['c_password']
	building_number = request.form['building_number']
	street = request.form['street']
	city = request.form['city']
	state = request.form['state']
	phone_number = request.form['phone_number']
	passport_number = request.form['passport_number']
	passport_expiration = request.form['passport_expiration']
	passport_country = request.form['passport_country']
	date_of_birth = request.form['date_of_birth']
#	if not len(password) >= 4:
#                flash("Password length must be at least 4 characters")
#               return redirect(request.url)
	cursor = conn.cursor()
	query = "SELECT * FROM customer WHERE email = \'{}\'"
	cursor.execute(query.format(email))
	data = cursor.fetchone()
	cursor.close()
	#use fetchall() if you are expecting more than 1 data row
	error = None
	if(data):
		#If the previous query returns data, then user exists
		error = "This user already exists"
		return render_template('register.html', error = error)
	else:
		ins = "INSERT INTO customer(email, name, password, building_number, street, city, state, phone_number, passport_number, passport_expiration, passport_country, date_of_birth) VALUES(\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\')"
		cursor = conn.cursor()
		cursor.execute(ins.format(email, name, password, building_number, street, city, state, phone_number, passport_number, passport_expiration, passport_country, date_of_birth))
		conn.commit()
		cursor.close()
		flash("You are logged in")
		return render_template('login.html', error= "Welcome! Please login~")



@app.route('/agent_registerAuth', methods=['GET', 'POST'])
def agent_registerAuth():
	email = request.form['b_email']
	password = request.form['b_password']
	booking_agent_id = request.form['b_ID']
#	if not len(password) >= 4:
#                flash("Password length must be at least 4 characters")
#               return redirect(request.url)
	cursor = conn.cursor()
	query = "SELECT * FROM booking_agent WHERE email = \'{}\'"
	cursor.execute(query.format(email))
	data = cursor.fetchone()
	#use fetchall() if you are expecting more than 1 data row
	error = None
	cursor.close()

	if(data):
		#If the previous query returns data, then user exists
		error = "This user already exists"
		return render_template('register.html', error = error)
	else:
		ins = "INSERT INTO booking_agent(email, password, booking_agent_id) VALUES(\'{}\', \'{}\', \'{}\')"
		cursor = conn.cursor()
		cursor.execute(ins.format(email, password, booking_agent_id))
		conn.commit()
		cursor.close()
		flash("You are logged in")
		return render_template('login.html', error= "Welcome! Please login~")


@app.route('/staff_registerAuth', methods=['GET', 'POST'])
def staff_registerAuth():
	username = request.form['a_username']
	first_name = request.form['first_name']
	last_name = request.form['last_name']
	password = request.form['a_password']
	date_of_birth = request.form['a_date_of_birth']
	airline_name = request.form["airline"]
#	if not len(password) >= 4:
#                flash("Password length must be at least 4 characters")
#               return redirect(request.url)
	cursor = conn.cursor()
	query = "SELECT * FROM airline_staff WHERE username = \'{}\'"
	cursor.execute(query.format(username))
	data = cursor.fetchone()
	#use fetchall() if you are expecting more than 1 data row
	error = None
	cursor.close()
	if(data):
		#If the previous query returns data, then user exists
		error = "This user already exists"
		return render_template('register.html', error = error)
	else:
		ins = "INSERT INTO airline_staff(username, password, first_name, last_name, date_of_birth, airline_name) VALUES( \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\')"
		cursor = conn.cursor()		
		cursor.execute(ins.format(username, password, first_name, last_name, date_of_birth, airline_name))
		conn.commit()
		cursor.close()
		flash("You are logged in")
		return render_template('login.html', error= "Welcome! Please login~")











#------------------------------------login----------------------------------------

@app.route('/cus_loginAuth', methods=['POST'])
def cusloginAuth():
	username = request.form['c_email']
	password = request.form['c_password']
	cursor = conn.cursor()
	query = "SELECT * FROM customer WHERE email = \'{}\' and password = \'{}\'"
	cursor.execute(query.format(username, password))
	data = cursor.fetchone()
	#use fetchall() if you are expecting more than 1 data row
	cursor.close()
	error = None
	if(data):
		session['username'] = username
		# cursor = conn.cursor()
		# query = "SELECT name FROM customer WHERE email = \'{}\'"
		# cursor.execute(query.format(username))
		# name = cursor.fetchone()
		# #use fetchall() if you are expecting more than 1 data row
		# cursor.close()
		# print(name)
		return render_template('home.html', type = "customer", name = username)	
	else:
		#returns an error message to the html page
		error = 'Invalid login or username'
		return render_template('login.html', error=error)


@app.route('/agent_loginAuth', methods=['POST'])
def agent_loginAuth():
	username = request.form['b_email']
	password = request.form['b_password']
	booking_agent_id = request.form["b_ID"]
	cursor = conn.cursor()
	query = "SELECT * FROM booking_agent WHERE email = \'{}\' and password = \'{}\' and booking_agent_id = \'{}\'"
	cursor.execute(query.format(username, password, booking_agent_id))
	data = cursor.fetchone()
	#use fetchall() if you are expecting more than 1 data row
	cursor.close()
	error = None
	if(data):
		session['username'] = username
		session['id'] = booking_agent_id
		print(username)
		return render_template('home.html', type = "agent", name = username)
	else:
		#returns an error message to the html page
		error = 'Invalid login or username'
		return render_template('login.html', error=error)


@app.route('/staff_loginAuth', methods=['POST'])
def staff_loginAuth():
	username = request.form['a_username']
	password = request.form['a_password']
	airline = request.form['airline']
	cursor = conn.cursor()
	query = "SELECT * FROM airline_staff WHERE username = \'{}\' and password = \'{}\' and airline_name = \'{}\'"
	cursor.execute(query.format(username, password, airline))
	data = cursor.fetchone()
	#use fetchall() if you are expecting more than 1 data row
	cursor.close()
	error = None
	if(data):
		session['username'] = username
		session['airline'] = airline
		return render_template('home.html', type = "staff", name = username)
	else:
		#returns an error message to the html page
		error = 'Invalid login or username'
		return render_template('login.html', error=error)









#--------------------------public-------------------------------------------

@app.route('/Search_byCity', methods = ["GET", "POST"])
def Search_byCity():
	# departure_city, arrival_city, departure_airport, arrival_airport, date
	departure_city = request.form["dep_city"]
	arrival_city = request.form["arr_city"]
	date = request.form["date_city"]
	cities=[departure_city,arrival_city]
	cursor = conn.cursor()
	file = open("./Queries/public_searchCity.sql","r")
	query = file.read()
	file.close()
	cursor.execute(query.format(departure_city, arrival_city, date))
	data1 = cursor.fetchall()
	cursor.close()

	try: 
		cursor = conn.cursor()
		query = "select email from booking_agent where email = \'{}\'"
		cursor.execute(query.format(session['username']))
		data2 = cursor.fetchone()
		cursor.close()
		is_agent = False
		if data2:
			is_agent = True
	except:
		is_agent = False

	return render_template('purchase.html', type = "city", cities=cities, posts=data1, is_agent = is_agent)

@app.route('/Search_byAirport', methods = ["GET", "POST"])
def Search_byAirport():
	departure_airport = request.form["dep_airport"]
	arrival_airport = request.form["arr_airport"]
	date = request.form["date_airport"]
	cursor = conn.cursor()
	file = open("./Queries/public_searchAirport.sql","r")
	query = file.read()
	file.close()
	cursor.execute(query.format(departure_airport, arrival_airport, date))
	data1 = cursor.fetchall()
	cursor.close()

	try: 
		cursor = conn.cursor()
		query = "select email from booking_agent where email = \'{}\'"
		cursor.execute(query.format(session['username']))
		data2 = cursor.fetchone()
		cursor.close()
		is_agent = False
		if data2:
			is_agent = True
	except:
		is_agent = False

	
	return render_template('purchase.html', type="airport", posts=data1, is_agent = is_agent)

@app.route('/Search_status', methods = ["GET", "POST"])
def Search_status(): 
	airline = request.form["airline"]
	flight_num = request.form["flight_num"]
	filterby = request.form["filter"]
	date = request.form["flight_date"]
	cursor = conn.cursor()
	if filterby == "dep_date":
		file = open("./Queries/public_searchStatus_byDepDate.sql","r")
		query = file.read()
		file.close()
		cursor.execute(query.format(flight_num, airline, date))
	else:
		file = open("./Queries/public_searchStatus_byArrDate.sql","r")
		query = file.read()
		file.close()
		cursor.execute(query.format(flight_num, airline, date))
	data1 = cursor.fetchall()
	cursor.close()
	return render_template('status.html', posts=data1)











#--------------------------customer_events-----------------------------------
@app.route('/cus_ViewFlight_default', methods = ["GET","POST"])
# @login_required
def cus_ViewFlight_default():
	date_lower = datetime.datetime.now()
	date_lower.strftime('%Y-%m-%d %H:%M:%S')
	date_upper = "9999-12-31"
	customer_email = session['username']
	cursor = conn.cursor()
	file = open("./Queries/cus_myFlight.sql","r")
	query = file.read()
	file.close()
	cursor.execute(query.format(customer_email, date_lower, date_upper))
	data1 = cursor.fetchall()
	cursor.close()
	print("!!!!!!!!!!!!!!!!!!!!!!!")
	print(data1)
	return render_template('flight.html', posts=data1)

@app.route('/cus_ViewFlight', methods = ["GET","POST"])
# @login_required
def cus_ViewFlight():
	# date_lower, date_upper
	date_lower = request.form["from"]
	date_upper = request.form["to"]
	customer_email = session['username']
	cursor = conn.cursor()
	file = open("./Queries/cus_myFlight.sql","r")
	query = file.read()
	file.close()
	cursor.execute(query.format(customer_email, date_lower, date_upper))
	data1 = cursor.fetchall()
	cursor.close()
	print("!!!!!!!!!!!!!!!!!!!!!!!")
	print(data1)
	return render_template('flight.html', posts=data1)

@app.route('/cus_Purchase', methods = ["GET", "POST"])
# @login_required
def cus_Purchase():
	#airline_name, flight_number
	# seats!!!!!!!!!!
	try:
		string = request.form["string"]
		m_list = string.split(",")
		airline_name = 	m_list[0]
		flight_number = int(m_list[1])
		customer_email = session["username"]
		#---check_ticketNumber---------
		cursor = conn.cursor()
		file = open("./Queries/checkPurchase.sql","r")
		query = file.read()
		file.close()
		cursor.execute(query.format(airline_name, flight_number))
		data2 = cursor.fetchall()
		cursor.close()
		if data2[0][1] - data2[0][0] <= 0:
			return "<br><br>The tickets for this flight is sold out, please try another one~"
			
		# print("!!!!!!!!!!!!!!!!!!!!!!!!!")
		# print(type(customer_email),customer_email)
		cursor = conn.cursor()
		query = "insert into ticket (airline_name, flight_num) values(\'{}\', \'{}\');"
		cursor.execute(query.format(airline_name, flight_number))
		conn.commit()
		cursor.close()

		cursor = conn.cursor()
		query = "insert into purchases(ticket_id, customer_email, purchase_date) values((select max(ticket_id) from ticket), \'{}\', curdate());"
		cursor.execute(query.format(customer_email))
		conn.commit()
		cursor.close()
		return "<br><br>You have successfully purchased the flight " + airline_name + str(flight_number) +" !"
	except:
		return render_template("login.html")


@app.route('/Track_my_spending', methods = ["GET", "POST"])
# @login_required
def Track_my_spending():
	date_lower = request.form["from"]
	date_upper = request.form["to"]
	customer_email = session['username']
	# if not date_lower:
	# 	date_lower = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	# if not date_upper:
	# 	date_upper = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	cursor = conn.cursor()
	file = open("./Queries/cus_mySpending.sql","r")
	query = file.read()
	file.close()
	cursor.execute(query.format(customer_email, date_lower, date_upper))
	data1 = cursor.fetchall()
	cursor.close()
	print(data1)
	return render_template('spending.html', name=customer_email, posts=data1)












#--------------------------agent_events-----------------------------------
@app.route('/agent_ViewFlight_default', methods = ["GET","POST"])
# @login_required
def agent_ViewFlight_default():
	date_lower = datetime.datetime.now()
	date_lower.strftime('%Y-%m-%d %H:%M:%S')	
	id = session['id']
	date_upper = "9999-12-31"
	cursor = conn.cursor()
	file = open("./Queries/agent_myFlight.sql","r")
	query = file.read()
	file.close()
	cursor.execute(query.format(id, date_lower, date_upper))
	data1 = cursor.fetchall()
	cursor.close()
	return render_template('flight_a.html', posts=data1)

@app.route('/agent_ViewFlight', methods = ["GET","POST"])
# @login_required
def agent_ViewFlight():
	# date_lower, date_upper
	date_lower = request.form["from"]
	date_upper = request.form["to"]
	id = session['id']
	# if not date_lower:
	# 	date_lower = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	# if not date_upper:
	# 	date_upper = "9999-12-31"
	cursor = conn.cursor()
	file = open("./Queries/agent_myFlight.sql","r")
	query = file.read()
	file.close()
	cursor.execute(query.format(id, date_lower, date_upper))
	data1 = cursor.fetchall()
	cursor.close()
	return render_template('flight_a.html', posts=data1)


@app.route('/agent_Purchase', methods = ["GET", "POST"])
# @login_required
def agent_Purchase():
	#airline_name, flight_number
	# seats!!!!!!!!!!
	string = request.form["string"]
	m_list = string.split(",")
	airline_name = 	m_list[0]
	flight_number = int(m_list[1])
	booking_agent_id = session['id']
	#-----------check_tickets------------
	cursor = conn.cursor()
	file = open("./Queries/checkPurchase.sql","r")
	query = file.read()
	file.close()
	cursor.execute(query.format(airline_name, flight_number))
	data2 = cursor.fetchall()
	cursor.close()
	if data2[0][1] - data2[0][0] <= 0:
		return "<br><br>The tickets for this flight is sold out, please try another one~"

	# print("!!!!!!!!!!!!!!!!")
	# print(booking_agent_id)
	customer_email = request.form["customer"]

	cursor = conn.cursor()
	query = "insert into ticket (airline_name, flight_num) values(\'{}\', \'{}\');"
	cursor.execute(query.format(airline_name, flight_number))
	conn.commit()
	cursor.close()

	cursor = conn.cursor()
	query = "insert into purchases(ticket_id, customer_email, booking_agent_id, purchase_date) values((select max(ticket_id) from ticket), \'{}\', \'{}\', curdate());"
	cursor.execute(query.format(customer_email, booking_agent_id))
	conn.commit()
	cursor.close()

	return "<br><br>You have successfully purchased the flight " + airline_name + " " + str(flight_number) + " for " + customer_email +" !"

@app.route('/agent_myCommission_dafault', methods = ["GET", "POST"])
# @login_required
def agent_myCommission_default():
	date_upper = datetime.datetime.now()
	date_upper.strftime('%Y-%m-%d')
	booking_agent_id = session["id"]
	interval = 1
	# if not date_lower:
	#  date_lower = "1971-01-01"
	# if not date_upper:
	#  date_upper = "9999-12-31"
	cursor = conn.cursor()
	file = open("./Queries/agent_myCommission.sql","r")
	query = file.read()
	file.close()
	cursor.execute(query.format(booking_agent_id, date_upper, interval, date_upper))
	data = cursor.fetchall()
	cursor.close()
	return render_template('commission.html', posts=data)



@app.route('/agent_myCommission', methods = ["GET", "POST"])
# @login_required
def agent_myCommission():
	date_lower = request.form["from"]
	date_upper = request.form["to"]
	booking_agent_id = session["id"]
	interval = 0
	# if not date_lower:
	#  date_lower = "1971-01-01"
	# if not date_upper:
	#  date_upper = "9999-12-31"
	cursor = conn.cursor()
	file = open("./Queries/agent_myCommission.sql","r")
	query = file.read()
	file.close()
	cursor.execute(query.format(booking_agent_id, date_lower, interval, date_upper))
	data = cursor.fetchall()
	cursor.close()
	return render_template('commission.html', posts=data)


@app.route('/agent_topCustomer', methods = ["GET", "POST"])
# @login_required
def agent_topCustomer():
	booking_agent_id = session["id"]
	Type = request.form["type"]
	date_upper = datetime.datetime.now()
	date_upper.strftime('%Y-%m-%d')
	cursor = conn.cursor()
	if Type == "By Commission":
		interval = 12
		file = open("./Queries/agent_topCustomers_byCommission.sql","r")
	else:
		interval = 6
		file = open("./Queries/agent_topCustomers_byNumber.sql","r")
	query = file.read()
	file.close()
	cursor.execute(query.format(booking_agent_id, date_upper, interval, date_upper))
	data1 = cursor.fetchall()
	cursor.close()
	print(data1)
	return render_template('top_customer.html', posts=data1, Type = Type)


#--------------------------staff_events-----------------------------------
@app.route('/staff_myFlight', methods = ["GET", "POST"])
# @login_required
def staff_myFlight():
	date_lower = request.form['from']
	date_upper = request.form['to']
	airline = session['airline']
	cursor = conn.cursor()
	file = open("./Queries/staff_myFlight.sql","r")
	query = file.read()
	file.close()
	cursor.execute(query.format(airline, date_lower, airline))
	data1 = cursor.fetchall()
	return render_template('flight_s.html', posts = data1)



@app.route('/staff_allCustomerForFlight', methods = ["GET", "POST"])
#@login_required
def staff_allCustomerForFlight():
	string = request.form["string"]
	m_list = string.split(",")
	airline_name = 	m_list[0]
	flight_number = int(m_list[1])
	#---
	cursor = conn.cursor()
	file = open("./Queries/staff_allCustomerForFlight.sql","r")
	query = file.read()
	file.close()
	cursor.execute(query.format(airline_name, flight_number))
	data1 = cursor.fetchall()
	return render_template('customer.html', posts = data1)

	


@app.route('/staff_createNewFlight', methods = ["GET", "POST"])
# @login_required
def staff_createNewFlight():
	#airline_name = request.form["airline_name"]
	airline_name = session['airline']
	flight_num = request.form["flight_num"]
	departure_airport = request.form["dep_airport"]
	departure_time = request.form["dep_time"]
	arrival_airport = request.form["arr_airport"]
	arrival_time  = request.form["arr_time"]
	price = request.form["price"]
	status = request.form["status"]
	airplane_id = request.form["airplane"]
	#check whether the flight exists
	cursor = conn.cursor()
	query = "select airline_name, flight_num from flight where airline_name = \'{}\' and flight_num = \'{}\'"
	cursor.execute(query.format(airline_name, flight_num))
	data1 = cursor.fetchall()
	cursor.close()
	if data1:
		return "<br><br>This flight already exists！"
	#------------------
	file = open("./Queries/staff_createNewFlight.sql","r")
	query = file.read()
	file.close()
	cursor = conn.cursor()
	cursor.execute(query.format(airline_name, flight_num, departure_airport, departure_time, arrival_airport, arrival_time, price, status, airplane_id))
	conn.commit()
	cursor.close()
	return "<br><br>You have successfully created flight " + flight_num + " for airline " + airline_name + " !"


@app.route('/staff_changeStatus', methods = ["GET", "POST"])
# @login_required
def staff_changeStatus():
	airline_name = session['airline']
	flight_num = request.form["s_flight_num"]
	status = request.form['n_status']
	#------------------
	file = open("./Queries/staff_changeStatus.sql","r")
	query = file.read()
	file.close()
	cursor = conn.cursor()
	cursor.execute(query.format(status, airline_name, flight_num))
	conn.commit()
	cursor.close()
	return "<br><br>You have successfully changed flight status of " +  airline_name + " " + flight_num + " to " + status + " !"

@app.route('/staff_addAirplane', methods = ["GET", "POST"])
# @login_required
def staff_addAirplane():
	airline_name = session['airline']
	airplane_id = request.form["n_airplane"]
	seats = request.form["seats"]
	#check whether the flight exists
	cursor = conn.cursor()
	query = "select airline_name, airplane_id from airplane where airline_name = \'{}\' and airplane_id = \'{}\'"
	cursor.execute(query.format(airline_name, airplane_id))
	data1 = cursor.fetchall()
	cursor.close()
	if data1:
		return "<br><br>This airplane already exists！"
	#------------------
	file = open("./Queries/staff_addAirplane.sql","r")
	cursor = conn.cursor()
	query = file.read()
	file.close()
	cursor.execute(query.format(airline_name, airplane_id, seats))
	conn.commit()
	cursor.close()
	return "<br><br>You have successfully added Airplane " + airplane_id + " for airline " + airline_name + " !"

@app.route('/staff_addAirport', methods = ["GET", "POST"])
# @login_required
def staff_addAirport():
	airport_name = request.form["airport"]
	city = request.form["city"]
	#check whether the flight exists
	cursor = conn.cursor()
	query = "select airport_name, airport_city from airport where airport_name = \'{}\' and airport_city = \'{}\'"
	cursor.execute(query.format(airport_name, city))
	data1 = cursor.fetchall()
	cursor.close()
	if data1:
		return "<br><br>This airport already exists！"
	#------------------
	file = open("./Queries/staff_addAirport.sql","r")
	cursor = conn.cursor()
	query = file.read()
	file.close()
	cursor.execute(query.format(airport_name, city))
	conn.commit()
	cursor.close()
	return "<br><br>You have successfully added Airport " + airport_name + " in city " + city + " !"

@app.route('/staff_topAgents', methods = ["GET", "POST"])
# @login_required
def staff_topAgents():
	Type = request.form["type"]
	airline = session['airline']
	date_upper = datetime.datetime.now()
	date_upper.strftime('%Y-%m-%d')
	interval = 1000
	#------------------
	if Type == "Tickets--past month":
		interval = 1
		file = open("./Queries/staff_topAgents_byNumber.sql","r")
	elif Type == "Tickets--past year":
		interval = 12
		file = open("./Queries/staff_topAgents_byNumber.sql","r")
	else:
		interval = 12
		file = open("./Queries/staff_topAgents_byCommission.sql","r")
	cursor = conn.cursor()
	query = file.read()
	cursor.execute(query.format(airline, date_upper, interval, date_upper))
	data1 = cursor.fetchall()
	file.close()
	cursor.close()
	print("!!!!!!!")
	print(data1)
	return render_template("top_agents.html", posts=data1, Type=Type)

@app.route('/staff_frequentCustomer', methods = ["GET", "POST"])
# @login_required
def staff_frequentCustomer():
	airline = session["airline"]
	date_upper = datetime.datetime.now()
	date_upper.strftime('%Y-%m-%d')
	interval = 12
	file = open("./Queries/staff_frequentCustomer.sql","r")
	cursor = conn.cursor()
	query = file.read()
	cursor.execute(query.format(airline, date_upper, interval, date_upper))
	data1 = cursor.fetchall()
	file.close()
	cursor.close()
	return render_template("frequent_customer.html", posts=data1)


@app.route('/staff_flightForCustomer', methods = ["GET", "POST"])
# @login_required
def staff_flightForCustomer():
	string = request.form["string"]
	m_list=string.split(",")
	customer_email = m_list[0]
	airline = session["airline"]
	file = open("./Queries/staff_flightForCustomer.sql","r")
	cursor = conn.cursor()
	query = file.read()
	cursor.execute(query.format(airline, airline, customer_email))
	data1 = cursor.fetchall()
	file.close()
	cursor.close()
	return render_template("detail.html", posts=data1)

@app.route('/staff_reports', methods = ["GET", "POST"])
# @login_required
def staff_reports():
	date_lower = request.form["from"]
	date_upper = request.form["to"]
	airline = session["airline"]
	#-----------------
	file = open("./Queries/staff_reports.sql","r")
	cursor = conn.cursor()
	query = file.read()
	cursor.execute(query.format(airline, date_lower, date_upper))
	data1 = cursor.fetchall()
	file.close()
	cursor.close()
	return render_template("report.html", posts=data1)

@app.route('/staff_topDestination', methods = ["GET", "POST"])
# @login_required
def staff_topDestination():
	airline = session["airline"]
	Type = request.form["type"]
	date_upper = datetime.datetime.now()
	date_upper.strftime('%Y-%m-%d')
	interval = 3
	if Type == "Last year":
		interval = 12
	file = open("./Queries/staff_topDestination.sql","r")
	cursor = conn.cursor()
	query = file.read()
	cursor.execute(query.format(airline,airline, date_upper, interval, date_upper))
	data1 = cursor.fetchall()
	file.close()
	cursor.close()
	return render_template("top_destinations.html", posts=data1)

@app.route('/staff_Revenue', methods = ["GET", "POST"])
# @login_required
def staff_Revenue():
	airline = session["airline"]
	date_upper = datetime.datetime.now()
	date_upper.strftime('%Y-%m-%d')
	Type = request.form["type"]
	interval = 1
	if Type == "Last year":
		interval = 12
	file = open("./Queries/staff_revenueCustomer.sql","r")
	cursor = conn.cursor()
	query = file.read()
	cursor.execute(query.format(airline, date_upper, interval, date_upper))
	data1 = cursor.fetchall()
	file.close()
	cursor.close()
	print("!!!!!!!!!")
	print(data1)
	file = open("./Queries/staff_revenueAgent.sql","r")
	cursor = conn.cursor()
	query = file.read()
	cursor.execute(query.format(airline, date_upper, interval, date_upper))
	data2 = cursor.fetchall()
	file.close()
	cursor.close()
	print("!!!!!!!!!")
	print(data2)
	return render_template("revenue.html", posts1=data1, posts2=data2)


#-------------------------------------------------------------------------
app.secret_key = 'some key that you will never guess'
#Run the app on localhost port 5000
#debug = True -> you don't have to restart flask
#for changes to go through, TURN OFF FOR PRODUCTION
if __name__ == "__main__":
	app.run('127.0.0.1', 5000, debug = True)
