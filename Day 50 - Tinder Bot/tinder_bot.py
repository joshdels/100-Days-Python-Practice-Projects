import os 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

my_email = os.environ.get('MAIN_EMAIL')
my_pass = os.environ.get('FB_PASSWORD')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://tinder.com/")


time.sleep(2)
log_in = driver.find_element(By.XPATH, value='//*[@id="s67002758"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a')
log_in.click()

time.sleep(2)
fb = driver.find_element(By.XPATH, value='//*[@id="s-1661378318"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
fb.click()

# change to other windows
time.sleep(2)
tinder_page = driver.window_handles[0]
fb_page = driver.window_handles[1]
driver.switch_to.window(fb_page)
print(driver)

# fb text entry
fb_email = driver.find_element(By.XPATH, value='//*[@id="email"]')
fb_email.send_keys(my_email, Keys.ENTER)
fb_passw = driver.find_element(By.XPATH, value='//*[@id="pass"]')
fb_passw.send_keys(my_pass, Keys.ENTER)
fb_log_in = driver.find_element(By.XPATH, value='//*[@id="u_0_0_08"]')
fb_log_in.click()

# # capcha
# capcha = driver.find_element(By.XPATH, value='//*[@id="«r1»"]')
# capcha.send_keys(input("Enter the capcha here"), Keys.ENTER)

# dyem capcha error to fb even though right entered


driver.switch_to.window(tinder_page)
print(driver.title)


driver = quit()


# NOTE that dangerous captcha hahaha
# ggwp close call! did not finish all due to that captcha and fb problems
# FB so bad it cancels me everyday!





