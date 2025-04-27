import requests
from bs4 import BeautifulSoup


url = 'https://appbrewery.github.io/Zillow-Clone/'
response = requests.get(url=url)
website = response.text


soup = BeautifulSoup(website, "html.parser")
card = soup.find_all("a")

for n in card:
    print(n.get_text())


# class Zillow:
#     def __init__(self):
#         '''gets link text in Zillow'''
#         self.zillow_url = 'https://appbrewery.github.io/Zillow-Clone/'
#         self.response = requests.get(url=self.zillow_url)
#         self.website = self.response.text
        
#     def get_appartments(self):
#         '''Returns the list of appartments within the criteria'''
#         soup = BeautifulSoup(self.website, "html.parser")
#         # extract list len
#         appartments = soup.find_all(name="ul", class_="List-c11n-8-84-3-photo-cards")
        
#         print(len(appartments))
#         for n in appartments:
#             print(n.get_text())      



#NOTE 
# go for functionality before going to oops!