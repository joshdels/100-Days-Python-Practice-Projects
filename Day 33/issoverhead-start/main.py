import os
import requests
from datetime import datetime
import smtplib
from dotenv import load_dotenv

#load correct file path
os.chdir(r"C:\Users\deleo\OneDrive\Documents\GitHub\100-Days-Python-Practice-Projects\Day 33\issoverhead-start")
load_dotenv()

my_email = os.getenv('MY_EMAIL')
my_password = os.getenv('PASSWORD')

MY_LONG =  28#125.665606 # Your longitude
MY_LAT = 48.4406#7.430135 # Your latitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
print(data)


#Your position is within +5 or -5 degrees of the ISS position.
def checker_iss():
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT- 5 <= iss_latitude <= MY_LAT+ 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        print("Yes its passing above")
        check_time()
    else: 
        print("bye its far")
        
def check_time():
    print(f"sunset {sunset}")
    print(f"sunrise {sunrise}")
    today_hour = int(time_now.strftime("%H"))
    print(f"today_hour {today_hour}")
    
    if sunset <= 18 <= sunrise:
        print("Time is gold")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(
                user=my_email,
                password = my_password,
                to_addrs=my_email,
                msg=f"Subject:ISS incoming\n\nLook up mate"
            )
            print("messege sent!")
    else:
        print("wala sa time")
    

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()


checker_iss()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

# print(data)








