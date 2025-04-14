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
        '''Retrieves data from the Google sheet'''
        try:
            response = requests.get(url=self.sheety_endpoint, headers=self.header)

        except requests.exceptions.RequestException as e:
            print("Quota Reached for Sheety! \n{e}")
        else:
            data = response.json()
            print(data)
            
        return data
    
    def fill_empty_iata(self, city_code, city_id):
        '''Replaces empty iataCode into proper one'''
        data = {
            "price":{
                'iataCode': city_code
                }
            }
        response = requests.put(url=f"https://api.sheety.co/54dcdd7e9ef50b78e3eeeaee2bfd74ca/flightDeals/prices/{city_id}", headers=self.header, json=data)
        
    def fill_prices(self, lowest_price, city_id):
        '''Send prices to the the google sheet'''
        data = {
            "price":{
                'lowestPrice' : lowest_price
                }
            }
        response = requests.put(url=f"https://api.sheety.co/54dcdd7e9ef50b78e3eeeaee2bfd74ca/flightDeals/prices/{city_id}", headers=self.header, json=data)
        print(response.text)