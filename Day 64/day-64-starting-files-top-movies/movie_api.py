import requests
import os

Movie_API = os.environ.get("MOVIE_API")
# Get the data
headers = {
  "accept": "application/json",
	'Authorization': f"Bearer {Movie_API}"
}

params = {
  "query": "spiderman"
}
response = requests.get(
	url="https://api.themoviedb.org/3/search/movie",
	params = params,
  headers=headers
)

data = response.json()
# print(data)

for row in data['results']:  
    id = row['id']
    title = row['title']
    date = row['release_date']
    
    print(id)
    print(title)
    print(date)


# url = f"https://api.themoviedb.org/3/movie/{id}"

# headers = {
#     "accept": "application/json",
#     "Authorization": f"Bearer {Movie_API}"
# }

# response = requests.get(url, headers=headers)

# # print(response.text)
# data = response.json()

# title = data['original_title']
# img_url = f"https://image.tmdb.org/t/p/w500/{data['poster_path']}"
# year = data['release_date'].split("-")[0]
# description = data['overview']

# print(title)
# print(img_url)
# print(year)
# print(description)