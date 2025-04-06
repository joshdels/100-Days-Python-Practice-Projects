import os
import datetime as dt
import random
import smtplib
from dotenv import load_dotenv

os.chdir(r"C:\Users\deleo\OneDrive\Documents\GitHub\100-Days-Python-Practice-Projects\Day 32\Birthday Wisher (Day 32) start")

load_dotenv()

my_email = os.getenv('MY_EMAIL')
my_password = os.getenv('PASSWORD')
to_email = os.getenv('TO_EMAIL')

list_of_quotes = []

# open files
with open("quotes.txt", mode='r') as quotes:
    quotes = quotes.readlines()
    for quote in quotes:
        stripped = quote.strip("\n") 
        list_of_quotes.append(stripped)
        
random_quote = random.choice(list_of_quotes)

# sends on 6th day of the week
now = dt.datetime.now()
day_of_week = now.weekday()

# send quote via email
if dt.datetime.now().weekday() == 6:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Quote of the Day\n\n{random_quote}"
        )
        print("Sent successfully")
else:
    print("Not today buddy")