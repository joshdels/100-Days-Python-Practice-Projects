import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

os.chdir(r"C:\Users\deleo\OneDrive\Documents\GitHub\100-Days-Python-Practice-Projects\Day 46")

spotify_id = os.environ.get("SPOTIFY_ID")
spotify_secret = os.environ.get("SPOTIFY_SECRET")
spotify_uri = os.environ.get("SPOTIFY_URI")

# scope = "user-library-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope = "playlist-modify-private playlist-modify-public",
    client_id=spotify_id,
    client_secret=spotify_secret,
    redirect_uri=spotify_uri,
    show_dialog=True,
    cache_path="token1.txt",)
    )

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: " )

billboard_url = "https://www.billboard.com/charts/hot-100/"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

full_url = f"{billboard_url}{date}/"

# web scrapping 100 billboards data
response = requests.get(url=full_url, headers=header)
# response.raise_for_status()
bill_board = response.text
soup = BeautifulSoup(bill_board, "html.parser")
songs = soup.select("li ul li h3")
song_list = [song.get_text().split()[0] for song in songs]
year = date.split("-")[0]
 
# finding URI for your song 
song_uris = []   
skipped = 0
for song in song_list:
    result = sp.search(q=f"track:{song} year: {year}", type="track")
    # print(result) 
    try:
        tracks = result["tracks"]
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
        # print(tracks)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped")
        skipped += 1
            
print(f"{skipped} skipped songs")

# creating a playlist and then adding a songs from the URI
user_id = sp.current_user()["id"]
playlist = sp.user_playlist_create(user_id, name=f"{date} Test Billboard 100", public=True)
print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)


# NOTE!
# medyo weak pa sa pag read og documentation, very confusing
# deym docu wa ko kasabot! hahaha