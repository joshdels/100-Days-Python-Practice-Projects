import requests
from bs4 import BeautifulSoup

date = input("Which year do you want to travel to? Tyoe the date in this format YYYY-MM-DD: " )

billboard_url = "https://www.billboard.com/charts/hot-100/"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

full_url = f"{billboard_url}{date}/"

response = requests.get(url=full_url, headers=header)
response.raise_for_status()
bill_board = response.text

soup = BeautifulSoup(bill_board, "html.parser")
songs = soup.select("li ul li h3")

song_list = [song.get_text().split() for song in songs]
print(song_list)

#soptify api