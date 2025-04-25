import os
from instant_follower import InstaFollower

my_email = os.environ.get('MY_TEST_EMAIL')
my_password = os.environ.get('GENERAL_PASSWORD')

insta_url = "https://www.instagram.com/"
name = 'chefsteps'
search_account_url = f"{insta_url}{name}/followers"

insta_bot = InstaFollower()
insta_bot.login(insta_url, my_email, my_password)

insta_bot.find_followers(search_account_url)


