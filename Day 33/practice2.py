import requests
from datetime import datetime

MY_LAT = 17.114543
MY_LONG = 17.831723
parameter = {
    "lat" :MY_LAT,
    "lng":MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameter)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

# print(sunrise.split("T")[1].split(":")[0]) #challenging spliting
print(sunrise)
print(sunset)

# print(data)
time_now = datetime.now()
print(time_now.hour)
