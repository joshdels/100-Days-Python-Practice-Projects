import os
path = os.chdir(r"C:\Users\deleo\OneDrive\Documents\GitHub\100-Days-Python-Practice-Projects\Day 25")

import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
size = data.groupby("Primary Fur Color").size() # very complicated my solution
print(size)

new_data = pandas.DataFrame(size)
new_data.to_csv("squirrel_count.csv")
print(new_data)

   






# Primary Fur Color
# How many primary fur color
# New data Frame