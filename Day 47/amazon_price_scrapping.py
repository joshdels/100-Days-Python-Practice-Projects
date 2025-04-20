import os
import requests
from bs4 import BeautifulSoup
import smtplib

my_email = os.environ.get("MY_TEST_EMAIL")
my_pass = os.environ.get("TEST_PASSWORD")

URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
header = {
    "Accept-Language": "en-US",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}
response = requests.get(URL, headers=header)
amazon_web = response.text

soup = BeautifulSoup(amazon_web, "html.parser")

# scrapes website
price_whole = soup.find(name="span", class_="a-price-whole").get_text()
price_decimal = soup.find(name="span", class_="a-price-fraction").get_text()
full_price = price_whole+price_decimal
name = soup.find(name="span", id="productTitle").get_text().strip()
device_name = ''.join(name)

# send email if price hits the target 
if float(full_price) < 100:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        print("Sending it to email")
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Amazon Pot discount!\n\nYour Favorite Pot {device_name} is on biggest sale! \n${full_price}".encode('utf-8')
        )
        print("Successfully Sent to email!")




# #9am everyday
# # checks price
# # target priuce
# # send email