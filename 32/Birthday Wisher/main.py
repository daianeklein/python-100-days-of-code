from dotenv import load_dotenv
import smtplib
import os

load_dotenv()
my_email = 'dklein.dev@gmail.com'
password = os.getenv('MY_PASSWORD_BIRTHDAY_WISHER')

connection = smtplib.SMTP('smtp.gmail.com', 587)
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs='daiane.klein22@gmail.com', msg = 'Hello!')
connection.close()
