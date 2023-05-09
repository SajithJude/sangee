import mysql.connector
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="zoo_management"
)
c = mydb.cursor()


def zoo_create_table():
	c.execute('CREATE TABLE IF NOT EXISTS zoo(zoo_id varchar(100) primary key not null,zoo_name varchar(100) NOT NULL, zoo_location varchar(100) NOT NULL, zoo_hours INT NOT NULL, zoo_contact bigint NOT NULL)')


def zoo_add_data(zoo_id, zoo_name, zoo_location, zoo_hours, zoo_contact):
	c.execute('INSERT INTO zoo(zoo_id, zoo_name, zoo_location, zoo_hours, zoo_contact) VALUES (%s,%s,%s,%s,%s)', (zoo_id, zoo_name, zoo_location, zoo_hours, zoo_contact))
	mydb.commit()


def zoo_view_all_data():
	c.execute('SELECT * FROM ZOO')
	data = c.fetchall()
	return data


def zoo_update_data(zoo_id, new_zoo_name, new_zoo_location, new_zoo_hours, new_zoo_contact):
	c.execute("UPDATE ZOO SET zoo_name=%s, zoo_location=%s, zoo_hours=%s, zoo_contact=%s WHERE zoo_id=%s ", (new_zoo_name, new_zoo_location, new_zoo_hours, new_zoo_contact, zoo_id))
	mydb.commit()
	data = c.fetchall()
	return data


def zoo_delete_data(zoo_id):
	c.execute('DELETE FROM ZOO WHERE zoo_id=%s', (zoo_id,))
	mydb.commit()

def cust_create_table():
	c.execute('CREATE TABLE IF NOT EXISTS CUSTOMER(cust_id varchar(100) PRIMARY KEY NOT NULL,cust_fname varchar(100) NOT NULL,cust_lname varchar(100) NOT NULL, cust_email varchar(100) NOT NULL, cust_address varchar(100) NOT NULL, cust_cred_no bigint NOT NULL)')


def cust_add_data(cust_id, cust_fname, cust_lname, cust_email, cust_address, cust_cred_no):
	c.execute('INSERT INTO CUSTOMER(cust_id, cust_fname, cust_lname, cust_email, cust_address, cust_cred_no) VALUES (%s,%s,%s,%s,%s,%s)', (cust_id, cust_fname, cust_lname, cust_email, cust_address, cust_cred_no))
	mydb.commit()


def cust_view_all_data():
	c.execute('SELECT * FROM CUSTOMER')
	data = c.fetchall()
	return data


def cust_update_data(cust_id, new_cust_fname, new_cust_lname, new_cust_email, new_cust_address, new_cust_cred_no):
	c.execute("UPDATE CUSTOMER SET cust_fname=%s, cust_lname=%s, cust_email=%s, cust_address=%s, cust_cred_no=%s WHERE cust_id=%s ", (new_cust_fname, new_cust_lname, new_cust_email, new_cust_address, new_cust_cred_no, cust_id))
	mydb.commit()
	data = c.fetchall()
	return data


def cust_delete_data(cust_id):
	c.execute('DELETE FROM CUSTOMER WHERE cust_id=%s', (cust_id,))
	mydb.commit()


def ticket_create_table():
	c.execute('CREATE TABLE IF NOT EXISTS TICKET(ticket_id varchar(100) not null,order_date date,price float,age int,primary key(ticket_id))')


def ticket_add_data(ticket_id, order_date, price, age):
	c.execute('INSERT INTO TICKET(ticket_id, order_date, price, age) VALUES (%s,%s,%s,%s)', (ticket_id, order_date, price, age))
	mydb.commit()


def ticket_view_all_data():
	c.execute('SELECT * FROM TICKET')
	data = c.fetchall()
	return data


def ticket_update_data(ticket_id, new_order_date, new_price, new_age):
	c.execute("UPDATE TICKET SET order_date=%s, price=%s , age=%s WHERE ticket_id=%s", (new_order_date, new_price, new_age, ticket_id))
	mydb.commit()
	data = c.fetchall()
	return data


def ticket_delete_data(ticket_id):
	c.execute('DELETE FROM TICKET WHERE ticket_id=%s', (ticket_id,))
	mydb.commit()


def emp_create_table():
	c.execute('CREATE TABLE IF NOT EXISTS EMPLOYEE(emp_id varchar(100) not null,emp_name varchar(100),emp_des varchar(100),phone_num bigint,salary float,primary key(emp_id))')


def emp_add_data(emp_id, emp_name, emp_des, phone_num, salary):
	c.execute('INSERT INTO EMPLOYEE(emp_id, emp_name, emp_des, phone_num, salary) VALUES (%s,%s,%s,%s,%s)', (emp_id, emp_name, emp_des, phone_num, salary))
	mydb.commit()


def emp_view_all_data():
	c.execute('SELECT * FROM EMPLOYEE')
	data = c.fetchall()
	return data


def emp_update_data(emp_id, new_emp_name, new_emp_des, new_phone_num, new_salary):
	c.execute("UPDATE EMPLOYEE SET emp_name=%s, emp_des=%s, phone_num=%s, salary=%s WHERE emp_id=%s", (new_emp_name, new_emp_des, new_phone_num, new_salary, emp_id))
	mydb.commit()
	data = c.fetchall()
	return data


def emp_delete_data(emp_id):
	c.execute('DELETE FROM EMPLOYEE WHERE emp_id=%s', (emp_id,))
	mydb.commit()


def animal_create_table():
	c.execute('CREATE TABLE IF NOT EXISTS ANIMAL(animal_id varchar(100) not null,animal_name varchar(100),cage_num varchar(100),gender varchar(100),height varchar(100),weight varchar(100),age varchar(100),diet varchar(100),status varchar(100),primary key(animal_id))')


def animal_add_data(animal_id, animal_name, cage_num, gender, height, weight,age,diet,status):
	c.execute('INSERT INTO ANIMAL(animal_id, animal_name, cage_num, gender, height, weight,age,diet,status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)', (animal_id, animal_name, cage_num, gender, height, weight,age,diet,status))
	mydb.commit()


def animal_view_all_data():
	c.execute('SELECT * FROM ANIMAL')
	data = c.fetchall()
	return data


def animal_update_data(animal_id, new_animal_name, new_cage_num, new_gender, new_height, new_weight,new_age,new_diet,new_status):
	c.execute("UPDATE ANIMAL SET animal_name=%s, cage_num=%s, gender=%s, height=%s, weight=%s, age=%s, diet=%s, status=%s  WHERE emp_id=%s", (new_animal_name, new_cage_num, new_gender, new_height, new_weight, new_age, new_diet, new_status, animal_id))
	mydb.commit()
	data = c.fetchall()
	return data


def animal_delete_data(animal_id):
	c.execute('DELETE FROM ANIMAL WHERE animal_id=%s', (animal_id,))
	mydb.commit()


def animal_view_count():
	c.execute('SELECT animal_count()')
	data = c.fetchall()
	return data

def animal_guide_promote():
	c.execute('call updtdemployee()')
	data = c.fetchall()
	return data


def ticket_discount():
	c.execute('select tkt_discount()')
	data = c.fetchall()
	return data

def children_visit_at_time():
	c.execute('call modify_ticket()')
	data = c.fetchall()
	return data





