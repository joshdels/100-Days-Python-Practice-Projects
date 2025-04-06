import os
import pandas
import datetime as dt
from dotenv import load_dotenv

os.chdir(r"C:\Users\deleo\OneDrive\Documents\GitHub\100-Days-Python-Practice-Projects\Day 32\Birthday Wisher (Day 32) start")

load_dotenv()

my_email = os.getenv('MY_EMAIL')
my_password = os.getenv('PASSWORD')

# time 
now = dt.datetime.now()
month = now.month #4
day = now.day #6

print(month)
print(day)

birthdays = {}
# user_birthday
birthday = pandas.read_csv("birthdays.csv")
print(birthday.columns)
birthdays = birthday.to_dict(orient='records')



# print(birthdays)


# create letter

# send letter