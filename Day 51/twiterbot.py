import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


PROMISED_DOWN = 100
PROMISED_UP = 100
twitter_email = os.environ.get('MY_TEST_EMAIL')
twitter_pass = os.environ.get('GENERAL_PASSWORD')
speed_test_url = "https://www.speedtest.net/"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get(speed_test_url)

#speed test
time.sleep(5)
print("starting")
start = driver.find_element(By.CLASS_NAME, value="js-start-test")
start.click()

result = driver.find_element(By.CLASS_NAME, value="result-data-large")
print("\n")
print("\n")
print(f"Naa na ang result: {result.text}")

# change = driver.find_element(By.CLASS_NAME, value="btn-server-select")

# print(change.text)
# change.click()




# TODO 1 speed test #done
# TODO 2 log in twitter
# TODO 3 send complaint from twiter