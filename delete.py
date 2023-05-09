import streamlit as st
from database import *


def zoo_delete():
	st.subheader("Delete Zoo Details")
	zoo_id = st.text_area("Zoo ID")
	if st.button(label="Delete"):
		zoo_delete_data(zoo_id)
		st.success("Successfully Deleted Data")


def cust_delete():
	st.subheader("Delete Customer Details")
	cust_id = st.text_area("Customer ID")
	if st.button(label="Delete"):
		cust_delete_data(cust_id)
		st.success("Successfully Deleted Data")


def ticket_delete():
	st.subheader("Delete Ticket Details")
	ticket_id = st.text_area("Ticket ID")
	if st.button(label="Delete"):
		ticket_delete_data(ticket_id)
		st.success("Successfully Deleted Data")


def emp_delete():
	st.subheader("Delete Employee Details")
	emp_id = st.text_area("Employee ID")
	if st.button(label="Delete"):
		emp_delete_data(emp_id)
		st.success("Successfully Deleted Data")


def animal_delete():
	st.subheader("Delete Animal Details")
	emp_id = st.text_area("Animal ID")
	if st.button(label="Delete"):
		emp_delete_data(emp_id)
		st.success("Successfully Deleted Data")

