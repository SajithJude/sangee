import pandas as pd
import streamlit as st
from database import *


def zoo_read():
	st.subheader("Zoo Details")
	zoo_result = zoo_view_all_data()
	with st.expander("View All Zoo Data"):
		zoo_clean_df = pd.DataFrame(zoo_result, columns=["ID", "Zoo Name", "Location", "Hour Open", "Contact"])
		st.dataframe(zoo_clean_df)


def cust_read():
	st.subheader("Customer Details")
	cust_result = cust_view_all_data()
	with st.expander("View All Customer Data"):
		cust_clean_df = pd.DataFrame(cust_result, columns=["Customer ID", "Customer First Name", "Customer Last Name", "Email", "Address", "Credit Card Number"])
		st.dataframe(cust_clean_df)


def ticket_read():
	st.subheader("Ticket Details")
	ticket_result = ticket_view_all_data()
	with st.expander("View All Ticket Data"):
		ticket_clean_df = pd.DataFrame(ticket_result, columns=["Ticket ID", "Order Date", "Price", "Age"])
		st.dataframe(ticket_clean_df)


def emp_read():
	st.subheader("Employee Details")
	emp_result = emp_view_all_data()
	with st.expander("View All Employee Data"):
		emp_clean_df = pd.DataFrame(emp_result, columns=["Employee ID", "Employee Name", "Employee Designation", "Phone Number", "Salary"])
		st.dataframe(emp_clean_df)


def animal_read():
	st.subheader("Animal Details")
	animal_result = animal_view_all_data()
	with st.expander("View All Animal Data"):
		animal_clean_df = pd.DataFrame(animal_result, columns=["Animal_id", "Animal_name", "Cage_Num", "Gender", "Height", "Weight", "Age", "Diet", "Status"])
		st.dataframe(animal_clean_df)


def animal_count():
	st.subheader("Animal Count")
	animal_result_2 = animal_view_count()
	with st.expander("View Animal Count"):
		animal_clean_df_2 = pd.DataFrame(animal_result_2, columns=["Count"])
		st.dataframe(animal_clean_df_2)


def children_visitor_count():
	st.subheader("Children Visitor Count")
	animal_result_3 = children_visit_at_time()
	with st.expander("View Child Visitor Count"):
		animal_clean_df_3 = pd.DataFrame(animal_result_3, columns=["Count"])
		st.dataframe(animal_clean_df_3)


def query_read(query):
	st.subheader("Query")
	c.execute(query)
	query_result = c.fetchall()
	with st.expander("View Query Result"):
		query_clean_df = pd.DataFrame(query_result, columns=["Query Result"])
		st.dataframe(query_clean_df)
