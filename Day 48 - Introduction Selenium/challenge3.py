from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

# Find the name keys
first_name = driver.find_element(By.NAME, value="fName")
first_name = driver.find_element(By.NAME, value="lName")
first_name = driver.find_element(By.NAME, value="email")

# Fill out form
first_name.send_keys("Joshua", Keys.ENTER)
first_name.send_keys("De Leon", Keys.ENTER)
first_name.send_keys("joshtest@gmail.com", Keys.ENTER)

# click submit
submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click()

driver.quit()