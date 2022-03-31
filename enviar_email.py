import smtplib
import ssl
from email.message import EmailMessage

subject = "Enviando emails por Python"
body = "Esse é um email teste!"
sender_email = "feresin.dev@gmail.com"
receiver_email = "de.edl1992@gmail.com"
password = input("Digite sua senha: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["subject"] = subject
message.set_content(body)


context = ssl.create_default_context()

print("Enviando Email!")

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Sucesso")