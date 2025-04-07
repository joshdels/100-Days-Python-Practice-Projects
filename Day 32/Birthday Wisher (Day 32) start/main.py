import os
import pandas
import datetime as dt
from dotenv import load_dotenv
import random
import smtplib

os.chdir(r"C:\Users\deleo\OneDrive\Documents\GitHub\100-Days-Python-Practice-Projects\Day 32\Birthday Wisher (Day 32) start")

load_dotenv()

my_email = os.getenv('MY_EMAIL')
my_password = os.getenv('PASSWORD')

# read csv files
def bday_file():
    random_number = random.randint(1,3)
    with open(f"letter_templates\letter_{random_number}.txt", 'r') as letter:
        my_letter = letter.read()
        modify_letter = my_letter.replace("[NAME]", name)
        
    return modify_letter

# time 
now = dt.datetime.now()
now_month = now.month #
now_day = now.day #

birthdays = {}

# user_birthday
birthday = pandas.read_csv("birthdays.csv")
birthdays = birthday.to_dict(orient='records')

#matching bday today of each user
for n in range(len(birthdays)):
    name = birthdays[n]['name']
    month = birthdays[n]['month']
    day = birthdays[n]['day']
    email = birthdays[n]['email']
    if month == now_month:
        if day == now_day:
            
            #send email via smtplib
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=email,
                    msg=f"Subject:Happy Bday\n\n{bday_file()}"
                )
                print("Sent successfully")

        
