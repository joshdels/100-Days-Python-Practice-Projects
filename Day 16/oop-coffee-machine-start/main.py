from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
menu.get_items()

drink = input("drinks?")

print(menu.find_drink(drink))

coffee_machine = CoffeeMaker()
coffee_machine.report()
print(coffee_machine.is_resource_sufficient())

#  wala ko kasabottt huhuhuuuuu need nakog practice whwahhaha