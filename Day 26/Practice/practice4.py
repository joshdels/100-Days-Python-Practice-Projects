import os
import pandas
path = os.chdir(r"C:\Users\deleo\OneDrive\Documents\GitHub\100-Days-Python-Practice-Projects\Day 26\Practice")

data = pandas.read_csv("Temperature.csv")

data_2020 = data[(data.YEAR == 2020) & (data["MONTH"].isin([12]))]

data_2020_dict = {row.DAY: row.TMAX for index, row in data_2020.iterrows()}

data_2020_df = pandas.DataFrame(list(data_2020_dict.items()), columns=["DAY", "TMAX"]) 
print(data_2020_df)
data_2020_df.to_csv("temp_data_dec.csv", index=False)



# data_2020_month = {row.YEAR: row.MONTH: row.DAY: row.TMAX for (index, row) in data.iterrows() if row.YEAR == 2020}
# print(data_2020_month)

# new_data = pandas.DataFrame(data_2020_month)
# new_data.to_csv("temp_2020.csv")
