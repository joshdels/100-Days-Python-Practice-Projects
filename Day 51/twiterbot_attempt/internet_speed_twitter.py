from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class InternetSpeedTwitterBot():
    def __init__(self):
        self.down = 0
        self.up = 0
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        
    def get_internet_speed(self, url):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(chrome_options)
        driver.get(url)

        #speed test
        time.sleep(5)
        print("starting")
        start = driver.find_element(By.CLASS_NAME, value="js-start-test")
        start.click()
        
        # speed data
        time.sleep(60)
        upload = driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.up = upload.text
        time.sleep(3)
        download = driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.down = download.text 
        
        driver.quit()
        


    def tweet_at_provider(self, url, email, password):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        
        driver = webdriver.Chrome(chrome_options)
        driver.get(url)
        
        time.sleep(2)
        login = driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a')
        login.click()
        
        time.sleep(2)
        email_input = driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        email_input.send_keys(email, Keys.ENTER)
        
        time.sleep(5)
        password_input = driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        password_input.send_keys(password, Keys.ENTER)
        
        time.sleep(2)
        user_input = driver.find_elements(By.XPATH, value='asdfasdf')
        user_input.send_keys(email, Keys.ENTER)
        
        time.sleep(5)
        password_input = driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        password_input.send_keys(password, Keys.ENTER)
        
        
        time.sleep(5)
        post = driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        post.click()
        
        time.sleep(2)
        write_post = driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/textarea')
        write_post.send_keys("asdfasdf", Keys.ENTER)
        
        time.sleep(2)
        submit = driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/button[2]')
        submit.click()
        

        
        