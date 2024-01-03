# # 100 days of code day 3 
# # Goals of today 
# # conditional statments
# # if else statments
# # depending on the conditions the flow of program is decided
# water_level = 50 
# if water_level > 80:
#     print("drained the water tank")
# else:
#     print("fill the tank")

# # purchase a rollercoaster ticket
# print("Welcome to the rollercoaster!!!")

# height = int(input("What is your height in cm? \n"))

# if height >= 120 :
#     print("Eligible to purchace the ticket... \n Successfully purchased the ticket you can ride the rollercoster")

# else:
#     print("You can not ride the rollercoaster....")

# # even or odd number 
# number = int(input("Enter the number: \n"))

# if number % 2 == 0:
#     print("This is an even number.")

# else:
#     print("This is an odd number.")

# # nested if statment 
# height = int(input("What is your heignt in cm : \n"))
# if height >= 120:
#     print("Eligible to purchace the ticket... \n Successfully purchased the ticket you can ride the rollercoster")
#     age = int(input("What is your age ?\n"))
#     if age >=18:
#         print("you need to pay full $12 ticket price.")
#     elif age <12:
#         print("You need to pay $5.")
#     else:
#         print("you age is under 18 you need to pay $7 ticket price.")
# else:
#     print("You can not ride the rollercoaster....")

# # Enter your height in meters e.g., 1.55
# height = float(input())
# # Enter your weight in kilograms e.g., 72
# weight = int(input())

# #Write your code below this line 👇
# BMI = weight/height**2
# if BMI < 18.5:
#   print(f"Your BMI is {BMI}, you are underweight.")
# elif BMI >=18.5 and BMI <25:
#   print(f"Your BMI is {BMI}, you have a normal weight.")
# elif BMI >= 25 and BMI <30:
#   print(f"Your BMI is {BMI}, you are slightly overweight.")

# elif BMI >=30 and BMI <35:
#   print(f"Your BMI is {BMI}, you are obese.")

# else:
#   print(f"Your BMI is {BMI}, you are clinically obese.")
  

# # Leap year check 
# # Which year do you want to check?
# year = int(input())
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇

# if year % 4 == 0 or year % 400 == 0 :
#   if year % 100 == 0:
#     print("Not leap year")
#   else:
#     print("Leap year")

# else:
#   print("Not leap year")

# # multiple conditions
# height = int(input("What is your heignt in cm : \n"))
# bill = 0
# if height >= 120:
#     print("Eligible to purchace the ticket... \n Successfully purchased the ticket you can ride the rollercoster")
#     age = int(input("What is your age ?\n"))
#     if age >=18:
#         bill = 12
#         print(" $12 Adult ticket price.")
#     elif age <12:
#         bill = 5
#         print("$5 Child Ticket.")
#     else:
#         bill = 7
#         print(" $7 teenager ticket price.")
#     photo = input("Do you want a photo ? Y or N \n")
#     if photo == "Y":
#         # add $3 dollars 
#         bill += 3

#     print(f"You need to pay $ {bill}")

# else:
#     print("You can not ride the rollercoaster....")
# print("Thank you for choosing Python Pizza Deliveries!")
# size = input() # What size pizza do you want? S, M, or L
# add_pepperoni = input() # Do you want pepperoni? Y or N
# extra_cheese = input() # Do you want extra cheese? Y or N
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇
# bill = 0
# if size == "S":
#   bill = 15
# elif size == "M":
#   bill = 20

# elif size == "L":
#   bill = 25
# if add_pepperoni == "Y":
#     if size == "S":
#        bill+=2
#     else:
#      bill +=3
# if extra_cheese == "Y":
#     bill +=1
  
# else:
#   print("Enter the size..!!!")
# print(f"Your final bill is: ${bill}.") 

# logical operators
# height = int(input("What is your heignt in cm : \n"))
# bill = 0
# if height >= 120:
#     print("Eligible to purchace the ticket... \n Successfully purchased the ticket you can ride the rollercoster")
#     age = int(input("What is your age ?\n"))
#     if age >= 45 and age<= 54:
#        bill = 0
#        print("You are eligible for midlife crisis.")
#     elif age >=18:
#         bill = 12
#         print(" $12 Adult ticket price.")
#     elif age <12:
#         bill = 5
#         print("$5 Child Ticket.")
#     else:
#         bill = 7
#         print(" $7 teenager ticket price.")
#     photo = input("Do you want a photo ? Y or N \n")
#     if photo == "Y":
#         # add $3 dollars 
#         if age >= 45 and age<= 54:
#             bill = 0
#         else:
#             bill += 3

#     print(f"You need to pay $ {bill}")

# else:
#     print("You can not ride the rollercoaster....")

# love calculator 

# print("The Love Calculator is calculating your score...")
# name1 = input() # What is your name?
# name2 = input() # What is their name?
# name1 = name1.lower()
# name2 = name2.lower()
# t1 = name1.count('t') +name1.count('r')+name1.count('u')+name1.count('e')
# l1 = name1.count('l') +name1.count('o')+name1.count('v')+name1.count('e')
# t2 = name2.count('t') +name2.count('r')+name2.count('u')+name2.count('e')
# l2 = name2.count('l') +name2.count('o')+name2.count('v')+name2.count('e')
# total = t1 +t2
# total1 = l1+l2
# total_love = str(total) + str(total1)
# lovescore = int(total_love)
# if lovescore <10 or lovescore> 90:
#   print(f"Your score is {lovescore}, you go together like coke and mentos. ")
# elif lovescore >40 and lovescore < 50:
#   print(f"Your score is {lovescore}, you are alright together.")
# else:
#   print(f"Your score is {lovescore}.")

# Treasue Island Game
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.\n Your mission is to find the treasure.")
dir = input("Your're at a cross road. Where do you want to go left of right?.\n")
if dir == "left":
  next = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat and type 'swim' to swim across.\n")
  if next == "wait":
    dorr = input("You arrived at the island. There is a huse with 3 doors. One Red, one blue and one yellow. Which color you want to choose? \n")
    if dorr == "red" or dorr == "blue":
      print("You entered the room of beast.! Game over.")
    if dorr == "yellow":
      print("Hurry you found the treasure...!!!")
  elif next == "swim":
    print("The water is full of aligators... Game Over")

  else:
    print("choose one option.")

elif dir == "right":
  print("You choose the wrong direction.. Game Over...")

else:
  print("Choose the one of the directions. ..")
