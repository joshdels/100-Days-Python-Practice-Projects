import os 
print(os.getcwd())
# os.chdir("c:/Users/deleo/OneDrive/Documents/GitHub/100-Days-Python-Practice-Projects/Day_24")

file = open(".\Day_24\my_files.txt")
contents = file.read()
print(contents)
file.close()

# with open("new_file.txt", mode="a") as file:
#     file.write("\nNew Text")
    