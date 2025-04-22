import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

linkedin_email = os.environ.get("LINKEDIN_TEST_EMAIL")
linledin_password = os.environ.get("LINKEDIN_PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4205699312&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")

# press sign in
time.sleep(5)
sign_in = driver.find_element(By.XPATH, value='//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
sign_in.click()

# # email and pass
time.sleep(2)
email = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal_session_key"]')
email.send_keys(linkedin_email, Keys.ENTER)
password = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal_session_password"]')
password.send_keys(linledin_password, Keys.ENTER)

# #submit
# time.sleep(2)
# submit = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')
# submit.click()


# save 
time.sleep(5)
save = driver.find_element(By.CSS_SELECTOR, value=".mt4 div .jobs-save-button")
save.click()

time.sleep(2)
follow = driver.find_element(By.CSS_SELECTOR, value=".mt5 .follow")
follow.click()

# follow button wont work but only hover hehehe
# ggwp selenium