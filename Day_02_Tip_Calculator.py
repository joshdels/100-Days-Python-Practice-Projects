'''
Drinking with friends with lunch
'''

print('Welcome to the tip calculator!')
bill = input('What was the total bill?: $')
tip = input("How much tip would you like to give? 10, 12, or 15?: ")
people = input("How many people to split the bill? ")

# Math Calculator
tip_to_pay = (float(bill) * (float(tip)/100)) / int(people)

# Results
print(f'Each person should pay: ${tip_to_pay}')