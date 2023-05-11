import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import streamlit as st


emaiid= st.text_input("Enter email")
if st.buttpon("Send"):
    message = Mail(
        from_email='muthulingam.thanoraj@flipick.com',
        to_emails='judesajith.aj@gmail.com',
        subject='Sending with Twilio SendGrid is Fun',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        st.write(response.status_code)
        st.write(response.body)
        st.write(response.headers)
    except Exception as e:
        st.write(e.message)