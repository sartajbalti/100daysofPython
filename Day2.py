#100days of code Day 2 practice session 
# # Data Types
# # String
# print("Hello"[0])
# print("Hello"[4])
# print("Hello"[1])

# # Integer
# print(1223+123)

# # Float
# print(3.1456)

# # Boolean
# print(True)

# # Type Error, Type Checking and Type Conversion
# # Type Error
# num_char = len(input("Whast is your name?"))
# # print("Your name have" + num_char + "character")

# # Type Checking
# print(type(num_char))

# # Type Conversion
# new_num_char = str(num_char)
# print("Your name have " + new_num_char + " characters")


# a = float(123)
# print(type(a))
# b = str(a)
# print(type(b))

# # # Mathematical Operations in Python
# # Addition
# print(3 + 5)

# # Subtraction
# print(7 - 4)

# # Multiplication
# print(3 * 2)

# # Division
# print(6 / 3)

# # Exponentiation
# print(2 ** 3)

# # PEMDASLR Rule
#     # Parentheses ()
#     # Exponents **
#     # Multiplication *
#     # Division /
#     # Addition +
#     # Subtraction -

# print(3*(3+3)/3-3)

# #round off the decimal and print in whole number 
# print(round(8/3))

# #BMI calculator
# # 1. Greetings
# print("Welcome to the BMI calculator")

# # 2. Ask the user for their height
# # height = float(input("What is your height in m ?\n"))

# # # 3. Ask the user for their weight
# # weight = float(input("What is your weight in kg ?\n"))

# # # 4. Calculate the BMI
# # bmi = weight / (height ** 2)

# # # 5. Print the BMI
# # # print("Your BMI is: ", round(bmi, 2))

# # # f-string
# # print(f"your BMI is {bmi}")

# # Number Manipulation and F Strings in Python
# print(round(2.3333333344445,5))

# print(8%2)

# re = 4/2
# re /= 2
# print(re)

# for i in range(0,100):
#     if i %2 == 0:
#         print("These are even numbers ",i)


print("Welcome to the tip calculator.")
bill = float(input("What was the total bill?$\n"))
tip = float(input("What percentage tip would you like to give?\n"))
people = int(input("How many people you want to split?\n"))
tip_amount = (bill*tip)/100
total_bill = bill + tip_amount
bill_per_person = total_bill / people
print(f"Each person should pay: $ 12{round(bill_per_person,2)}")


# # we are gonna make a tip calculator in todays session
# # 1. Greetings
# print("Welcome to the tip calculator")
# # 2. Ask the user for the total bill
# bill = float(input("What was the total bill ?\n"))
# # 3. Ask the user for the tip percentage they want to give
# tip = int(input("What percentage tip would you like to give ? 10, 12, or 15 ?\n"))
# # 4. Ask the user for the number of people to split the bill
# people = int(input("How many people to split the bill ?\n"))
# # 5. Calculate the tip amount
# tip_amount = (bill * tip) / 100
# # 6. Calculate the total bill
# total_bill = bill + tip_amount
# # 7. Calculate the bill per person
# bill_per_person = total_bill / people
# # 8. Print the bill per person
# print("Each person should pay: ", bill_per_person)
# # 9. Print the total bill
# print("The total bill is: ", total_bill)
# # 10. Print the tip amount
# print("The tip amount is: ", tip_amount)
# # 11. Print the bill per person upto 2 decimal places
# print("Each person should pay: ", round(bill_per_person, 2)) 