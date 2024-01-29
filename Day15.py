# cofee making machine

# Creat a code for coffee machine 
# three hot flavours Espresso, latte, Cappuccino 
#  different price 
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# print report
# Check resources sufficient?
# coins quarters, dimes, nickles, pennies
# process transaction successfull 
# make coffe deduct resources 
def update_resources(cof):
    for items in MENU[cof]['ingredients']:
        resources[items] = resources[items]- MENU[cof]['ingredients'][items]
def check_resources(cof):
    for items in MENU[cof]['ingredients']:
        if resources[items] <MENU[cof]['ingredients'][items]:
            return f"Sorry {items} is not enough"
        
def change_money(total,cof):
    change = total-MENU[cof]['cost']
    return change

def report():
    return f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}"

def coin():
    # total_amount = penny*0.01+dime*0.1+nickel*0.05+quarter*0.25
    total_amount = int(input("How many penny's: "))*0.01
    total_amount += int(input("How many dimes's: "))*0.1
    total_amount += int(input("How many nickel's: "))*0.05
    total_amount += int(input("How many quarter's: "))*0.25
    return total_amount

money = 0
# user_choice = input("What would you like? (espresso/latte/cappuccino): ")
# update_resources(user_choice)
# for items in MENU[user_choice]['ingredients']:
#     print(items)
# print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}")
is_on = True
while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice =='report':
        print(report())
    elif user_choice=="off":
                is_on = False
    else:
        if check_resources(user_choice) is None:
            
            total_money= coin()
            if total_money<MENU[user_choice]['cost']:
                print(f"The coffee costs {MENU[user_choice]['cost']} and the amount is not enough.")
                total_money= coin()
                remaining = change_money(total_money,user_choice)
                money += MENU[user_choice]['cost']
                print(f"Here is ${remaining} in change.")
                print(f"Here is your {user_choice} ☕ Enjoy!")
                update_resources(user_choice)
            else:
                remaining = change_money(total_money,user_choice)
                money += MENU[user_choice]['cost']
                print(f"Here is ${remaining} in change.")
                print(f"Here is your {user_choice} ☕ Enjoy!")
                update_resources(user_choice)

            
            
        else:
            print(check_resources(user_choice))
            refill = input("Want to refill? Type 'y' or 'n'") 
            if refill == 'y':
        
                if resources['coffee']>=80 and resources["milk"]>=200 and resources["water"]>=300:
                    print(f"Already enough incrideints")
                else:
                    resources["coffee"]+=10
                    resources["milk"]+=50
                    resources["water"]+=100
            else:
                print("Sorry we the coffee machine is turned off")
                is_on = False
            
    # print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}")
    
