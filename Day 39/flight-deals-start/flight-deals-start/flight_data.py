import requests
from flight_search import FlightSearch

class FlightData(FlightSearch):
    #This class is responsible for structuring the flight data.
    def __init__(self):
        super().__init__()
        self.url = "https//test.api.amadeus.com/v2/shopping/flights-offers"
        
        self.authorize_header_prices = {
            "Authorization": f"Bearer {self.get_token()}"
        } 
        
        
        
    def search_prices(self, data):
        for city in data:
            query = {
               "destinationLocationCode": city['iataCode'],
               "originLocationCode": "DVO",
               "adults": 1,
               "travelClass": "ECONOMY",
               "currencyCode": "PHP",
               "departureDate": "2025-10-02"
               }
            
            response = requests.get(url=self.url, params=query, headers=self.authorize_header)
            print(response.text)