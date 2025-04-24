import os
from internet_speed_twitter import InternetSpeedTwitterBot
import time

speed_test_url = "https://www.speedtest.net/"
twitter_url = "https://x.com"
twitter_email = os.environ.get('MY_TEST_EMAIL')
twitter_password = os.environ.get('SECOND_PASSWORD')

bot = InternetSpeedTwitterBot()
bot.get_internet_speed(speed_test_url)

print(bot.up + bot.down)

if float(bot.up) < 60:
    print("oi up is low!")
    bot.tweet_at_provider(twitter_url, twitter_email, twitter_password)
    
if float(bot.up) < 60:
    print("oi down is low!")
    bot.tweet_at_provider(twitter_url, twitter_email, twitter_password)
    
    
# i hate the captcha authenticate! it wont go pass dyem! 
# anyways it was fun to get it 











# # TODO 1 speed test #done
# # TODO 2 log in twitter
# # TODO 3 send complaint from twiter