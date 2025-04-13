#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData


flight_search = FlightSearch()


sheety = DataManager()
sheet_data = sheety.get_data()

for city in sheet_data:
    city_name = city['city']
    if city['iataCode'] == "":
        city_code = city['iataCode']
        city_code = flight_search.get_IATA_code(city_name)
        city_id = city['id']
        sheety.send_data(city_code, city_id)

print(sheet_data) # for checking data

flight_data = FlightData()



        
        
    
