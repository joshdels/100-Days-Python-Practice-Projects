# list comprehension
numbers = [1,2,3]
new_list = []

# list comprehension
new_list = [n + 1 for n in numbers]
print(new_list)

name = "Joshua"
new_list = [letter for letter in name]
print(new_list)


new_range = [num*2 for num in range(1,5)]
print(new_range)

# list comprehension with conditions
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)