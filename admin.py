from app import *
from database import *
import streamlit as st
if __name__ == '__main__':

    zoo_create_table()
    cust_create_table()
    ticket_create_table()
    animal_create_table()
    emp_create_table()
    menu = ["Admin"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Admin":
        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password", type='password')
        # if st.sidebar.button("Login"):
        if username == 'admin' and password == 'admin':
            main()
