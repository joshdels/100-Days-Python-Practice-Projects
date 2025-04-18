import requests
import os
from bs4 import BeautifulSoup

os.chdir(r"C:\Users\deleo\OneDrive\Documents\GitHub\100-Days-Python-Practice-Projects\Day 45\Starting Code - 100 movies to watch start")

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
# using request to connect to the website
response = requests.get(URL)
websites = response.text

# webscrapping stuffs
soup = BeautifulSoup(websites, "html.parser")
titles = soup.find_all(name="h3", class_="title")

movie_list = [title.getText() for title in titles]
reversed_movie_list = movie_list[::-1]

# stores in txt file
with open("movies.txt", mode="w", encoding="utf-8") as file:
    for title in reversed_movie_list:
        file.write(f"{title}\n")
