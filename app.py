from create import *
from read import *
from update import *
from delete import *
from database import *


def main():
    st.title("Zoo Management")
    menu = ["Zoo Details", "Customer Details", "Ticket Details", "Employee Details", "Animal Details","Run Queries"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Zoo Details":
        menu = ["Add", "View", "Update", "Delete"]
        choice1 = st.sidebar.selectbox("Menu", menu)
        if choice1 == "Add":
            zoo_create()
        elif choice1 == "View":
            zoo_read()
        elif choice1 == "Update":
            zoo_update()
        elif choice1 == "Delete":
            zoo_delete()
        else:
            st.subheader("Enter Correct Choice")

    elif choice == "Customer Details":
        menu = ["Add", "View", "Update", "Delete"]
        choice1 = st.sidebar.selectbox("Menu", menu)
        if choice1 == "Add":
            cust_create()
        elif choice1 == "View":
            cust_read()
        elif choice1 == "Update":
            cust_update()
        elif choice1 == "Delete":
            cust_delete()
        else:
            st.subheader("Enter Correct Choice")
    elif choice == "Ticket Details":
        menu = ["Add", "View", "Update", "Delete"]
        choice1 = st.sidebar.selectbox("Menu", menu)
        if choice1 == "Add":
            ticket_create()
        elif choice1 == "View":
            ticket_read()
        elif choice1 == "Update":
            ticket_update()
        elif choice1 == "Delete":
            ticket_delete()
        else:
            st.subheader("Enter Correct Choice")
    elif choice == "Employee Details":
        menu = ["Add", "View", "Update", "Delete"]
        choice1 = st.sidebar.selectbox("Menu", menu)
        if choice1 == "Add":
            emp_create()
        elif choice1 == "View":
            emp_read()
        elif choice1 == "Update":
            emp_update()
        elif choice1 == "Delete":
            emp_delete()
        else:
            st.subheader("Enter Correct Choice")
    elif choice == "Animal Details":
        menu = ["Add", "View", "Update", "Delete"]
        choice1 = st.sidebar.selectbox("Menu", menu)
        if choice1 == "Add":
            animal_create()
        elif choice1 == "View":
            animal_read()
            animal_count()
        elif choice1 == "Update":
            animal_update()
        elif choice1 == "Delete":
            animal_delete()
        else:
            st.subheader("Enter Correct Choice")
    elif choice == "Run Queries":
        query = st.text_area("Enter the Query")
        if st.button("Add Query"):
            query_read(query)
            st.success("Successfully Added Data")





