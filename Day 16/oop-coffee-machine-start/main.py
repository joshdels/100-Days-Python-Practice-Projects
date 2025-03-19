from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# constructor
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine() 

coffee = menu.get_items()
coffee_list = coffee.split("/")

#choose drink

is_choosing_coffee = True
checking = True
while is_choosing_coffee:
    while checking:
        user_coffee = input(f"what is your drink print({coffee}: )")
        if user_coffee == 'report':
            coffee_maker.report()
            money_machine.report()
        elif user_coffee in coffee_list:
            # cost of coffee
            coffee_items = menu.find_drink(user_coffee)
            cost_of_coffee = coffee_items.cost
            break
        else:
            print(f"Please enter correctly {coffee}")

    # coffee proceeding
    if coffee_maker.is_resource_sufficient(coffee_items):
        # coffee_maker.make_coffee()
        print("resources are available")
        #make payment
        money_machine.make_payment(cost_of_coffee)
        coffee_maker.make_coffee(coffee_items)
        #compute remaining resources
        
    else:
        print("insufficint resources returning your money")
    
#fun game ggs!
# better read the documentation and its function need parameters