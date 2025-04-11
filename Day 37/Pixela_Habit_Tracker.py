import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "joshuadels"
TOKEN = "123123123"
ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# CREATES THE USER ACCOUNT
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": ID,
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# ADDS A COLORFUL GRAPH 
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today = datetime.now()
print(today.strftime("%Y%m%d"))


pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you run today?"),
}

#ADDS PIXEL TO THE GRAPH
response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/20250323"
update_config = {
    "quantity": "3.0"
}

# # UPDATE THE DETAIL OF THE GRAPH
# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response.text)


update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/20250323"

# # DELETE THE DETAIL OF THE GRAPH
# response = requests.delete(url=update_endpoint, headers=headers)
# print(response.text)

