from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
        
        # time to debug
        time.sleep(5)
        followers = self.driver.find_element(By.XPATH, value='//*[@id="mount_0_0_kf"]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a/span')
        followers.click()
        
        # scroll = self.driver.find_element(By.XPATH, value='/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        # scroll.send_keys(Keys.END)
        # time.sleep(2)
        # following = self.driver.find_elements(By.XPATH, value='//*[@id="mount_0_0_5P"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div[2]/div[1]/div')
        # for n in range(following):
        #     print(following[n].get_attribute("button"))
        
 
        
    