"""
Practice for loops and if else statement
1/15/2025
"""

print("FizzBuzz\n")
#List comprehension 
list_num = [num for num in  range(1,101)]

#Condition checking

for i in list_num:
    if i % 3 == 0 and i %5 == 0:
        print("FizzBuzz!")
    elif i % 3 ==0:
        print("Fizz")
    elif i % 5 ==0:
        print("Buzz")
    else:
        print(i)
