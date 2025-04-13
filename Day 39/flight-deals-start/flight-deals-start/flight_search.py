import requests
import os

class FlightSearch:
    '''This class is responsible for talking to the Flight Search API'''
    def __init__(self): 
        self.flight_api_key = os.environ.get('FLIGHTS_API_KEY')
        self.flight_api_secret = os.environ.get('FLIGHTS_API_SECRET')
        self.flight_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
        
        self.data = {
            "grant_type":"client_credentials",
            "client_id" : self.flight_api_key,
            "client_secret" :self.flight_api_secret 
        }
        self.header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
    def get_token(self):
        '''Returns the access token'''
        response = requests.post(url=self.flight_endpoint, headers=self.header, data=self.data)
        data = response.json()
        access_token = data["access_token"]
        
        return access_token
    
    def get_IATA_code(self, city_name):
        self.parameters = {
            "keyword": city_name
        }
        
        self.authorize_header = {
            "Authorization": f"Bearer {self.get_token()}"
        }
        
        response = requests.get(url="https://test.api.amadeus.com/v1/reference-data/locations/cities", params=self.parameters, headers=self.authorize_header)
        retrieved_data = response.json()
        iata_code = retrieved_data["data"][0]['iataCode']
        print(iata_code)
        
        return iata_code
    