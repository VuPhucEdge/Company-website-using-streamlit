import smtplib
import ssl
import os


def send_email(message, user_email):
    host = 'smtp.gmail.com'
    port = 465

    username = 'vuphucjava@gmail.com'
    password = 'zzujkvvacrzezwnt'

    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, user_email, message)
