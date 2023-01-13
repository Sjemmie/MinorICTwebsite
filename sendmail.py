import os
import smtplib
import ssl

# send email function
def send_email(message):
    host = 'smtp.gmail.com'
    port = 465

    username = "youridibbetgames@gmail.com"
    password = os.getenv('GPP')

    receiver = "minormyldd@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
