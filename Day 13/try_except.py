try:
    age = int(input("Your age: "))
except ValueError:
    # i think it will rerun only once....
    print("You type wrong, please entry valid number like 15: ")
    age = int(input("Your age: "))

if age > 18:
    print("Holy you are 18+")