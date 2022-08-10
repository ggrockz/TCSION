import smtplib
from email.mime.text import MIMEText
import registor

def send_message():


    email_body_info = "Hi, you have been successfully registered your mailid"

    #print(address_info ,email_body_info)

    sender_email = "gyaneshtcs@gmail.com"

    sender_password = "qqnvihbvkxzisutr"

    server = smtplib.SMTP('smtp.gmail.com' ,587)

    server.starttls()

    server.login(sender_email ,sender_password)

    print("Login successful")

    server.sendmail(sender_email ,"shivame2011@gmail.com" ,email_body_info)

    print("Message sent")


