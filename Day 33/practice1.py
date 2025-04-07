import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

#json data
data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

#convert to tupple
iss_position = (longitude, latitude)

print(iss_position)

    
