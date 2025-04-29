from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Forms:
    def __init__(self):
        
        self.url = 'https://docs.google.com/forms/d/1eygXRHH626GJ4Om4Visv1pZgFyha8fkMC-hf5msehyA/edit'
        
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_experimental_option("detach", True)
        
        self.driver = webdriver.Chrome(chrome_option)
        self.driver.get(self.url)


    def insert_info(self, property, price, link):
        '''writes the data to the google form'''
        time.sleep(1)
        self.property = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        self.property.send_keys(property, Keys.ENTER)
        
        self.price = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        self.price.send_keys(price, Keys.ENTER)
        
        self.link = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        self.link.send_keys(link, Keys.ENTER)
        
        self.submit = self.driver.find_element(By.XPATH, value = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
        self.submit.click()
        
        self.new_form = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        self.new_form.click()
