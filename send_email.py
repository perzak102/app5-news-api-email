import smtplib, ssl, time
import os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465


    username = "mlody.inwestor.1950@gmail.com"
    password = "fxsxzqogudhcbicn"

    receiver = "perzak102@wp.pl"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)




