import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv('MY_EMAIL')
my_password = os.getenv('PASSWORD')
to_email = os.getenv('TO_EMAIL')
# print(password)


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs=to_email, 
        msg="Subject:Hello\n\nThis is a test using smtp") 