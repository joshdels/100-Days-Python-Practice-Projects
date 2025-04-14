#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData

flight_search = FlightSearch()
sheety = DataManager()
flight_data = FlightData()

sheet_data = sheety.get_data()
print(sheet_data)

# for missing iataCode
for city in sheet_data:
    city_name = city['city']
    city_id = city['id']
    
    if city['iataCode'] == "":
        city_code = flight_search.get_IATA_code(city_name)
        sheety.fill_empty_iata(city_code, city_id)
    
    lowest_price = flight_data.find_cheapest_prices(sheet_data)
    sheety.fill_prices(lowest_price, city_id)

print(sheet_data) # for checking datas

        
        
    
