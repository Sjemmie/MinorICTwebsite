import smtplib

import streamlit as st
from sendmail import send_email

st.header("Contact Us")
st.write("Voor vragen zijn wij via het onderstaande formulier te bereiken")
keuze_menu = "Website", "Feedback", "Overig"

try:
    with st.form(key="email_form", clear_on_submit=True):
        user_email = st.text_input("email", placeholder='Vul je hier je emailadres in', label_visibility='collapsed')
        topic = st.selectbox("Waar gaat je vraag over?", options=(keuze_menu))
        raw_message = st.text_area("message", placeholder='Vul hier je vraag in', label_visibility='hidden')
        message = f'''\
    Subject: New email from {user_email}
    
    Onderwerp: {topic}
    {raw_message}
    '''

        user_send = st.form_submit_button()
        if user_send:
            send_email(message)
            st.info('Your email was send successfully')
            st.balloons()
except smtplib.SMTPResponseException:
    st.info("This page is currently under review, it will be up and running momentarily."
            " Your message has not been delivered due to this issue. We hope you understand!")
    st.balloons()