MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 500,
    "milk": 200,
    "coffee": 100,
}

MONEY = 0

def report(user_resources, user_money):
    '''check resources are sufficient'''
    water = user_resources['water']
    milk = user_resources['milk']
    coffee = user_resources['coffee']
    
    print(f"Water: {water}ml")
    print(f"Water: {milk}ml")
    print(f"Water: {coffee}g")
    print(f"Money: ${user_money}")

def insert_coins():
    # process coin
    # - insert coins, quarter, dimes nickles, pennies
    print("Please insert coins.")
    quarter = int(input("How many  quarters? "))

    dimes =  int(input("How many  dimes? ") )
    nickles = int(input("How many  nickles? ")) 
    pennies = int(input("How many  pennies? "))
    
    return float(round(quarter*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01, 2))

# - calculate change
def process(user_money, machine_resources, user_prompt, machine_menu):
    '''takes user to calculate resources and calculate change if needed'''
    coffee_ingredients = machine_menu[user_prompt]['ingredients']
    coffee_cost = machine_menu[user_prompt]['cost']
    # compare machine resources and user_promt resources
    if user_money >= coffee_cost:
        if coffee_ingredients['water'] <= machine_resources['water'] and coffee_ingredients['milk'] <= machine_resources['milk'] and coffee_ingredients['coffee'] <= machine_resources['coffee']:
            # - transaction successful
            # - calculate change
            change = user_money - coffee_cost
            print(f"sucessful, here is your{user_prompt}☕, returning your change ${change}")
            
            # update resoures --- needs debugging
            machine_resources['water'] -= coffee_ingredients['water']
            machine_resources['coffee'] -= coffee_ingredients['coffee']
            machine_resources['milk'] -= coffee_ingredients['milk']
            
        else:
            # - sorry not enough, refund
            print(f"insufficient ingredients for {user_prompt}, returning money ${user_money}")
        
    else:
        # - sorry not enough, refund 
        print(f"Insufficient Coins. You've inserted ${user_money}  coints, the {user_prompt} is ${coffee_cost}, returning money")
    
        
        
machine_is_on = True
while machine_is_on:
    promt = input("What would you like? (espresso/latte/cappuccino): ")
    # add off
    if promt == 'off':
        print("Turning off the coffee machine")
        machine_is_on = False
    elif promt == 'report':
        report(resources, MONEY)
    elif promt in ['espresso', 'latte', 'cappuccino']:
        MONEY += insert_coins()
        process(MONEY, resources, promt, MENU)
        MONEY = 0
        
    else: 
        print("Please enter correctly")
        
        
        

# reflection
# happy finished it strong, chunking into smaller pieces is sheeeshhh! works on me
# sucessful one