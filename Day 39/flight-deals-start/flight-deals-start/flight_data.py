import requests
from flight_search import FlightSearch

class FlightData(FlightSearch):
    #This class is responsible for structuring the flight data.
    def __init__(self):
        super().__init__()
        self.url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        
        self.authorize_header_prices = {
            "Authorization": f"Bearer {self.get_token()}"
        } 
        
        
        
    def find_cheapest_prices(self, data):
        code = data[0]['iataCode']
        
        query = {
            "destinationLocationCode": code,
            "originLocationCode": "DVO",
            "adults": 1,
            "travelClass": "ECONOMY",
            "currencyCode": "PHP",
            "departureDate": "2025-11-02"
            }
            
        response = requests.get(url=self.url, params=query, headers=self.authorize_header_prices)
        data_price = response.json()
        
        for n in range(len(data_price)):
            price_flight = data_price['data'][n]['price']['total']
            cheapest_price = float(price_flight)
            if float(price_flight) < cheapest_price:
               cheapest_price = float(price_flight)
            
        return cheapest_price
        