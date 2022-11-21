import streamlit as st
from sendmail import send_email

st.header("Contact Us")
st.write("Voor vragen zijn wij via het onderstaande formulier te bereiken")

with st.form(key="email_form", clear_on_submit=True):
    user_email = st.text_input('', placeholder='Vul je hier je emailadres in')
    raw_message = st.text_area("", placeholder='Vul hier je vraag in')
    message = f'''\
Subject: New email from {user_email}
{raw_message}
'''
    user_send = st.form_submit_button()
    if user_send:
        send_email(message)
        st.info('Your email was send successfully')