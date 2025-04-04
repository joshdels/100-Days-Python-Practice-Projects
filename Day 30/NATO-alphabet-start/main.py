import os
import pandas
path = os.chdir(r"C:\Users\deleo\OneDrive\Documents\GitHub\100-Days-Python-Practice-Projects\Day 30\NATO-alphabet-start")



data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}

# my method
# is_searching = True
# while is_searching:
#     try:
#         my_name = input("What is your name?: ").upper()
#         output_list = [nato_alphabet[letter] for letter in my_name]
#         print(output_list)
        
#         is_searching = False
        
#     except KeyError:
#         print(f"Sorry, only letters in the alphabet")
        
# i Used while loops, while the correct answer is use a method
def generate_phonetic():
    my_name = input("What is your name?: ").upper()
    try:
        output_list = [nato_alphabet[letter] for letter in my_name]
    except KeyError:
        print(f"Sorry, only letters in the alphabet")
        generate_phonetic()
    else:
        print(output_list)
        
generate_phonetic()










