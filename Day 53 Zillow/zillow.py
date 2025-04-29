import requests
from bs4 import BeautifulSoup
    
class Zillow:
    def __init__(self):
        url = 'https://appbrewery.github.io/Zillow-Clone/'
        response = requests.get(url)
        self.website = response.text
        self.soup = BeautifulSoup(self.website, "html.parser")
        
        self.price_list = []
        self.address_list = []
        self.link_list = []
    
    def get_data(self):
        '''Gets the data from zillow.com'''
        #price
        price = self.soup.select(".List-c11n-8-84-3-photo-cards li div div article div div div div span")
        for n in price:
            self.price_list.append(n.get_text().replace("/mo", "").split("+")[0])
            
        #address
        address = self.soup.select(".List-c11n-8-84-3-photo-cards li div div article div div a address")
        for n in address:
            self.address_list.append(n.get_text().replace(" | ", " ").strip())
        
        #link
        link = self.soup.select(".List-c11n-8-84-3-photo-cards li div div article div div a")
        for n in link:
            self.link_list.append(n['href'])
        
        
    
    




                    


    

#TODO 1 Create a list of prices
#TODO 2 Create a list of links
#TODO 3 Create a list of address


#NOTE 
# go for functionality before going to oops!

# Clean up the address data as well. Remove any newlines, pipe symbols |, and unnecessary whitespace.