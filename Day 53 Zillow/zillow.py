import requests
from bs4 import BeautifulSoup

class Zillow:
    def __init__(self):
        '''gets link text in Zillow'''
        self.zillow_url = 'https://appbrewery.github.io/Zillow-Clone/'
        self.response = requests.get(url=self.zillow_url)
        self.website = self.response.text
        
    def get_appartments(self):
        '''Returns the list of appartments within the criteria'''
        self.soup = BeautifulSoup(self.website, "html.parser")
        # extract list len
        self.list = self.soup.find_all(name="ul", class_="List-c11n-8-84-3-photo-cards")
        print(len(self.list))