from selenium import webdriver
from selenium.webdriver.common.by import By

# to control browser not to close
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# ====== by class_name =======
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")

# ====== by search bars ========
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)

# ======== by xpath =====
bug_link = driver.find_element(By.XPATH, value='//*[@id="success-stories"]/a')
print(bug_link.text)

# ======== mytiple ==========


# driver.close()
driver.quit()