from zillow import Zillow
from forms import Forms

website = Zillow()
forms = Forms()

website.get_data() 
 
adress_list = website.address_list
price_list = website.price_list
link_list = website.link_list

for n in range(len(price_list)):
    forms.insert_info(adress_list[n], price_list[n], link_list[n])
    


#TODO 1 scrape zillow bellow 3k using beautiful soup, zillow 
    # review nato ang beautiful soup by doing few exercises
#TODO 2 fill out google forms using selenium
#TODO 3 view finish outputs, google docs


#NOTE 
# mas ni better ang code, ganna review more on sa list comprehensions
# ka lami sa feeling na na solve nimo urahhh!









