from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options)
        
    def login(self, insta_url, my_email, my_password):
        self.driver.get(insta_url)

        time.sleep(2)
        email = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
        email.send_keys(my_email, Keys.ENTER)

        password = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
        password.send_keys(my_password, Keys.ENTER)
        
        time.sleep(6)
        save_login_prompt = self.driver.find_element(By.XPATH, value="//div[contains(text(), 'Not now')]")
        if save_login_prompt:
            save_login_prompt.click()
            
    def find_followers(self, url):
        # change url
        time.sleep(2) 
        self.driver.get(url)
        
        time.sleep(5)
        chefsteps_follower = self.driver.find_element(By.CSS_SELECTOR, f'ul li div a[href="/chefsteps/followers/"]')
        chefsteps_follower.click()
        
        time.sleep(2)
        followers = self.driver.find_elements(By.XPATH, value='/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers)
            time.sleep(2)
        
    def following(self):
        all_button = self.driver.find_elements(By.XPATH, value='/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/div/div/div[3]/div/button')    
        
        for button in all_button:
            try:
                button.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, value="//button[contains(text(), 'Cancel)]")
                cancel_button.click()
    
 
        
    