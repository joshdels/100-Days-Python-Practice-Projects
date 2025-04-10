import os
import requests
import datetime 
import smtplib


date_now = datetime.datetime.now().date()
date_yesterday = date_now - datetime.timedelta(days=1)
date_last_yesterday = date_now - datetime.timedelta(days=2)


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_END_POINT = "https://www.alphavantage.co/query"
NEWS_END_POINT = "https://newsapi.org/v2/everything"
alpha_api_key = os.environ.get("ALPHA_API_KEY")
news_api_key = os.environ.get("NEWS_API_KEY")
my_pass = os.environ.get("TEST_PASSWORD")
my_email = os.environ.get("MY_TEST_EMAIL")
print(my_email)
print(my_pass)


alpha_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alpha_api_key
}

news_parameters = {
    "apiKey": news_api_key,
    "q": COMPANY_NAME
}

response = requests.get(url=ALPHA_END_POINT, params=alpha_parameters)
response.raise_for_status()
alpha_data = response.json()

price_today = alpha_data["Time Series (Daily)"][str(date_yesterday)]['4. close']
price_yesterday = alpha_data["Time Series (Daily)"][str(date_last_yesterday)]['4. close']
price_percentage = round((float(price_today) - float(price_yesterday))/ float(price_today) *100, 2)


response = requests.get(url=NEWS_END_POINT, params=news_parameters)
response.raise_for_status()
news_data = response.json()

all_news = []
for n in range(3):
    news_dictionary = {}
    title = news_data['articles'][n]["title"]
    description = news_data['articles'][n]["description"]
    news_dictionary.update({"title": title, "description": description}) 
    all_news.append(news_dictionary)


symbol = ""
if price_percentage > 0:
    symbol = "🔺"
else:
    symbol = "🔻"
    
if price_percentage > 10:
    for n in all_news:       
        print(f"{STOCK}: {symbol} {price_percentage}%\nHeadline: {all_news[0]['title']}\nBrief: {all_news[0]['description']}\n")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(
            user=my_email,  
            password=my_pass,
            to_addrs=my_email,
            mfg=f"Subject:Test Stock Sender\n\n{STOCK}: {symbol} {price_percentage}%\nHeadline: {all_news[0]['title']}\nBrief: {all_news[0]['description']}\n"
        )
        print("messege sent!")
        
    
    
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
# """
# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# or
# "TSLA: 🔻5%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# """

