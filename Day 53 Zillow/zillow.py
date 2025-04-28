import requests
from bs4 import BeautifulSoup
import re


url = 'https://appbrewery.github.io/Zillow-Clone/'
response = requests.get(url=url)
website = response.text


soup = BeautifulSoup(website, "html.parser")
price = soup.select(".List-c11n-8-84-3-photo-cards li div div article div div div div span")

# this is for getting the price, needs cleaning
price_list = []
for n in price:
    price_list.append(n.get_text().strip())
    



address = soup.select(".List-c11n-8-84-3-photo-cards li div div article div div a address")

# address not yet!
address_list = []
for n in address_list:
    address_list.append(n.get_text())
    


# link done
link = soup.select(".List-c11n-8-84-3-photo-cards li div div article div div a")
link_list = []
for n in link:
    link_list.append(n['href'])
    
    
# print(price_list) 
print(address_list)
print(link_list)




                    


    

#TODO 1 Create a list of prices
#TODO 2 Create a list of links
#TODO 3 Create a list of address


#NOTE 
# go for functionality before going to oops!

# Clean up the address data as well. Remove any newlines, pipe symbols |, and unnecessary whitespace.