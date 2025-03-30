import pandas
import os


path = os.chdir(r"C:\Users\deleo\OneDrive\Documents\GitHub\100-Days-Python-Practice-Projects\Day 25")
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
grey_count = len(grey_squirrels)
red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
red_count = len(red_squirrels)
black_squirrels = data[data["Primary Fur Color"] == "Black"]
black_count = len(black_squirrels)

new_data = {
    "Fur Color": ["Grey", "Red", "Blackk"],
    "Squirel Count": [grey_count, red_count, black_count]
}
df = pandas.DataFrame(new_data)
df.to_csv("squirel_count_solution.csv")
