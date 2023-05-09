import streamlit as st
from database import *


def zoo_create():
	st.subheader("Add Zoo Details")

	col1, col2 = st.columns(2)

	with col1:
		zoo_id = st.text_area("Enter the Zoo ID")
		zoo_name = st.text_area("Enter the Zoo Name")
		zoo_location = st.text_area("Enter the Zoo Location")
	with col2:
		zoo_hours = st.text_area("Enter the Hours Open")
		zoo_contact = st.text_area("Enter the Contact Info")

	if st.button("Add Zoo Details"):
		zoo_add_data(zoo_id, zoo_name, zoo_location, zoo_hours, zoo_contact)
		st.success("Successfully Added Data")


def cust_create():
	st.subheader("Add Customer Details")

	col1, col2 = st.columns(2)

	with col1:
		cust_id = st.text_area("Enter the Customer ID")
		cust_fname = st.text_area("Enter the Customer First Name")
		cust_lname = st.text_area("Enter the Customer Last Name")
	with col2:
		cust_email = st.text_area("Enter the Customer Email")
		cust_address = st.text_area("Enter the Customer Address")
		cust_cred_no = st.text_area("Enter the Customer Credit Number")
	if st.button("Add Customer Details"):
		cust_add_data(cust_id, cust_fname, cust_lname, cust_email, cust_address, cust_cred_no)
		st.success("Successfully Added Data")


def ticket_create():
	st.subheader("Add Ticket Details")

	col1, col2 = st.columns(2)

	with col1:
		ticket_id = st.text_area("Enter the Ticket ID")
		order_date = st.text_area("Enter the Ticket Order date")
	with col2:
		age = st.text_area("Enter the Age")
	if st.button("Add Ticket Details"):
		ticket_add_data(ticket_id, order_date, 100, age)
		st.success("Successfully Added Data")


def emp_create():
	st.subheader("Add Employee Details")

	col1, col2 = st.columns(2)

	with col1:
		emp_id = st.text_area("Enter the Employee ID")
		emp_name = st.text_area("Enter the Employee Name")
	with col2:
		emp_des = st.text_area("Enter the Employee Designation")
		phone_num = st.text_area("Enter the Phone Number")
		salary = st.text_area("Enter the Salary")
	if st.button("Add Employee Details"):
		emp_add_data(emp_id, emp_name, emp_des, phone_num, salary)
		st.success("Successfully Added Data")


def animal_create():
	st.subheader("Add Animal Details")

	col1, col2, col3 = st.columns(3)

	with col1:
		animal_id = st.text_area("Enter the Animal ID")
		animal_name = st.text_area("Enter the Animal Name")
		cage_num = st.text_area("Enter the Cage Number")
	with col2:
		gender = st.text_area("Enter the Gender")
		height = st.text_area("Enter the Height")
		weight = st.text_area("Enter the Weight")
	with col3:
		age = st.text_area("Enter the Age")
		diet = st.text_area("Enter the Diet")
		status = st.text_area("Enter the Status")
	if st.button("Add Animals Details"):
		animal_add_data(animal_id, animal_name, cage_num, gender, height, weight, age, diet, status)
		st.success("Successfully Added Data")



