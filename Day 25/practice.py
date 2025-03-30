import os
path = os.chdir(r"C:\Users\deleo\OneDrive\Documents\GitHub\100-Days-Python-Practice-Projects\Day 25")

# with open("weather_data.csv") as data:
#     data = data.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as data:
#     data = csv.reader(data)
#     temperatures = []
#     for row in data:
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data)) #dataframe
# print(data["temp"])

#data frame like a spreadsheet
# data_dict = data.to_dict()
# print(data_dict)

# #data series
# temp_list = data["temp"].to_list()
# print(temp_list)

# #average
# ave = sum(temp_list)/(len(temp_list))
# print(ave)

# print(data["temp"].mean())

# print(data["temp"].max())

# # get data in column
# print(data["condition"])
# print(data.condition)

# # get data in Rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()]) #max temp of row
# monday = data[data.day == "Monday"]
# print(monday.temp * 9/5 + 32)

# Create a data frame from scratch
data_dict = {
    "students": ["Amy", "Jame", "Josh"],
    "scores": [76, 56, 90]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)