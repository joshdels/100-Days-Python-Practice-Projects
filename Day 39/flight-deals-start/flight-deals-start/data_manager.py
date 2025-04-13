import requests
import os

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_endpoint = "https://api.sheety.co/54dcdd7e9ef50b78e3eeeaee2bfd74ca/flightDeals/prices"
        self.basic_auth = os.environ.get('BASIC_SHEETY')
        
        self.header = {
            "Authorization": f"Basic {self.basic_auth}"
        }
        
    def get_data(self):
        response = requests.get(url=self.sheety_endpoint, headers=self.header)
        data = response.json()
        sheet_data = data["prices"]
        
        return sheet_data
    
    def send_data(self, city_code, city_id):
        data = {
            "price": 
                {'iataCode': city_code}
            }
        response = requests.put(url=f"https://api.sheety.co/54dcdd7e9ef50b78e3eeeaee2bfd74ca/flightDeals/prices/{city_id}", headers=self.header, json=data)
        print(response.text)