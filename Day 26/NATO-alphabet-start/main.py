import os
import pandas
path = os.chdir(r"C:\Users\deleo\OneDrive\Documents\GitHub\100-Days-Python-Practice-Projects\Day 26\NATO-alphabet-start")

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
my_name = input("What is your name?: ").upper()

# # my attempt
# my_name_list = [name for name in my_name]
# for name in my_name_list:
#     print(nato_alphabet[name])

output_list = [nato_alphabet[letter] for letter in my_name]
print(output_list)

# Reflection it takes a lot of time
# im nstill adopting list comprehension with df and dictionary quite hard






