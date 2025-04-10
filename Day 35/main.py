import requests
import os
api_key = os.environ.get("OWN_API_KEY")
MY_LAT = 0.655990
MY_LONG = 120.803400

# saving own Enviroment
#$env:OWN_API_KEY="YOUR_API_KEY" --> saving it to environments


parameter = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameter)
response.raise_for_status()
data = response.json()

will_rain = False
for n in range(4):
    weather_id = data['list'][n]['weather'][0]['id']
    if int(weather_id) < 700:
        will_rain = True
        
if will_rain:
    print("Bring an umbrella")
    
    
    
    

