import requests
from bs4 import BeautifulSoup

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
titleline = soup.find_all(name='a', class_="storylink")

article_texts= []
article_links = []

for titles in titleline:
    text = titles.getText()
    article_texts.append(text)
    link = titles.get("href")
    article_links.append(link)
    
article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_="score")]
larget_number = max(article_upvote)
article_index = article_upvote.index(larget_number)


print(article_texts)
print(article_links)
print(article_upvote)

#getting the largest text
print(article_texts[article_index])
print(article_links[article_index])





# print(article_texts)
# print(article_texts)

