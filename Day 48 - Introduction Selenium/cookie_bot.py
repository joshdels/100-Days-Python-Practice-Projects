from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

#find elements
cookie = driver.find_element(By.CSS_SELECTOR, value="#cookie")
store = driver.find_elements(By.CSS_SELECTOR, value="#store div b")
store_item = driver.find_elements(By.CSS_SELECTOR, value="#store div")

def get_price_list():
    items = []
    prices = []
    for n in range(len(store)):
        item = store[n].text.split("-")
        if item != ['']:
            items.append(item)
            
    for n in range(len(items)):
        clean_price = items[n][1].replace(',', '').strip()
        prices.append(clean_price)
        
    return prices

  
game = True
timeout = time.time() + 7
five_minutes = time.time() + 60*5

while game:
    print("wala pay 5 seconds")
    cookie.click()
    cookie = driver.find_element(By.CSS_SELECTOR, value="#cookie")
    store = driver.find_elements(By.CSS_SELECTOR, value="#store div b")
    store_item = driver.find_elements(By.CSS_SELECTOR, value="#store div")
    money = int((driver.find_element(By.CSS_SELECTOR, value="#money").text))
    
    if time.time() > timeout:
        print(" 5 seconds na")
        price_list = get_price_list()
        for price in reversed(price_list):
            if money >= int(price):
                index = price_list.index(price)
                buy_item = store_item[index]
                buy_item.click()
                


# nice try ggwp
            

