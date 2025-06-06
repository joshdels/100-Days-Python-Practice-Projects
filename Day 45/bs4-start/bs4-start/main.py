import os
from bs4 import BeautifulSoup
import lxml

os.chdir(r'C:\Users\deleo\OneDrive\Documents\GitHub\100-Days-Python-Practice-Projects\Day 45\bs4-start\bs4-start')
# print(os.listdir())

with open('website.html') as file:
    data = file.read()

#beautiful Soup
soup = BeautifulSoup(data, 'html.parser')
# print(soup.title.string)

# print(soup.prettify())

# print(soup.p)

# all_anchor_tags = soup.find_all(name="a")


# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

heading = soup.find(name="h1",id="name")
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))

company_url = soup.select_one(selector="#name")
print(company_url)

headings = soup.select(".heading")
print(headings)