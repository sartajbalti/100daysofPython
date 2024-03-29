# Object oriented programming (OOP)
# classes and objects
#  How to use OOP
# attributes(variables) and methods (functions)
# objects created from class 
# class CarBlueprint:
#     print("Cars")
# car = CarBlueprint()
from prettytable import PrettyTable
# Create a PrettyTable object
table = PrettyTable()

# Define table columns
# table.field_names = ["Name", "Age", "City"]
table.add_column("Name",["Jhon","Mehdi","Sartaj"])
table.add_column("City",["Skardu","Gamba","Roundu"])
# table.align =''
# Add data rows
# table.add_row(["John", 30, "New York"])
# table.add_row(["Alice", 25, "San Francisco"])
# table.add_row(["Bob", 35, "Seattle"])

# Print the table
print(table)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
is_on = True
Machine = MoneyMachine()
Coffee = CoffeeMaker()
menu = Menu()
while is_on:
    options = menu.get_items()
    user_choice = input(f"Which do you want? ({options}): ")
    
    if user_choice =="off":
        is_on=False
    elif user_choice == 'report':
        Coffee.report()
        Machine.report()
    else:
        items = menu.find_drink(user_choice)
        if items:
            if Coffee.is_resource_sufficient(items) and Machine.make_payment(items.cost):
                Coffee.make_coffee(items)
        # else:
        #     can_make = False
# if user_choice == 'report':
#     f"{CoffeeMaker().report()}\n{MoneyMachine().report()}"
# else:
#     if Menu().find_drink(user_choice) in Menu().get_items():
#         penny = int(input("How many Penny's: "))
    