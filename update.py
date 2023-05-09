import pandas as pd
import streamlit as st
from database import *
from read import *

def zoo_update():
	st.subheader("Update Zoo Details")
	col1, col2 = st.columns(2)

	with col1:
		zoo_id = st.text_area("Enter the Zoo ID")
		new_zoo_name = st.text_area("Enter the New Zoo Name")
		new_zoo_location = st.text_area("Enter the New Zoo Location")
	with col2:
		new_zoo_hours = st.text_area("Enter the New Hours Open")
		new_zoo_contact = st.text_area("Enter the New Contact Info")
	if st.button("Update Zoo Details"):
		zoo_update_data(zoo_id, new_zoo_name, new_zoo_location, new_zoo_hours, new_zoo_contact)
		st.success("Successfully Updated Data")


def cust_update():
	st.subheader("Update Customer Details")
	col1, col2 = st.columns(2)

	with col1:
		cust_id = st.text_area("Enter the Customer ID")
		new_cust_fname = st.text_area("Enter the New Customer First Name")
		new_cust_lname = st.text_area("Enter the New Customer Last Name")
	with col2:
		new_cust_email = st.text_area("Enter the New Email")
		new_cust_address = st.text_area("Enter the New Address")
		new_cust_cred_no = st.text_area("Enter the New Credit Card Number")
	if st.button("Update Customer Details"):
		cust_update_data(cust_id, new_cust_fname, new_cust_lname, new_cust_email, new_cust_address, new_cust_cred_no)
		st.success("Successfully Updated Data")


def ticket_update():
	st.subheader("Update Ticket Details")
	col1, col2 = st.columns(2)

	with col1:
		ticket_id = st.text_area("Enter the Ticket ID")
		new_order_date = st.text_area("Enter the Ticket Order date")
	with col2:
		new_age = st.text_area("Enter the Age")
	if st.button("Update Ticket Details"):
		ticket_update_data(ticket_id, new_order_date, 100, new_age)
		st.success("Successfully Updated Data")
	if st.button("Ticket Discount For Underage"):
		ticket_discount()
	if st.button("Count of Children on a particular date"):
		children_visitor_count()


def emp_update():
	st.subheader("Update Employee Details")
	col1, col2 = st.columns(2)

	with col1:
		emp_id = st.text_area("Enter the Employee ID")
		new_emp_name = st.text_area("Enter the Employee Name")
	with col2:
		new_emp_des = st.text_area("Enter the Employee Designation")
		new_phone_num = st.text_area("Enter the Phone Number")
		new_salary = st.text_area("Enter the Salary")
	if st.button("Update Employee Details"):
		emp_update_data(emp_id, new_emp_name, new_emp_des, new_phone_num, new_salary)
		st.success("Successfully Updated Data")
	if st.button("Increment Animal Guide Salary"):
		animal_guide_promote()

def animal_update():
	st.subheader("Update Animal Details")
	col1, col2, col3 = st.columns(3)

	with col1:
		animal_id = st.text_area("Enter the Animal ID")
		new_animal_name = st.text_area("Enter the Animal Name")
		new_cage_num = st.text_area("Enter the Cage Number")
	with col2:
		new_gender = st.text_area("Enter the Gender")
		new_height = st.text_area("Enter the Height")
		new_weight = st.text_area("Enter the Weight")
	with col3:
		new_age = st.text_area("Enter the Age")
		new_diet = st.text_area("Enter the Diet")
		new_status = st.text_area("Enter the Status")
	if st.button("Update Animal Details"):
		animal_update_data(animal_id, new_animal_name, new_cage_num, new_gender, new_height, new_weight, new_age, new_diet, new_status )
		st.success("Successfully Updated Data")



