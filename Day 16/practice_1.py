from turtle import Turtle, Screen
# construct an object
timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

#-----------------------

from prettytable import PrettyTable
# pretty tables practice for downloading a packages

# construct a object
table = PrettyTable()

table.field_names = ["Pokemon Name", "Type"]
table.add_rows([
    ["Pickachu", "Electric"],
    ["Squirtle", "Water"],
    ["Charmander", "Fire"]
])
table.align = "c"

print(table)