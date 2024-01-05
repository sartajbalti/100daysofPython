# Loops 
# is to repeat over and over again 
#  First for loop

# baltistan = ["roundu","skardu","shigar"]

# for balti in baltistan:
#     print(balti + " valley")

# # Input a Python list of student heights
# student_heights = input().split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# total = 0
# students = 0
# for i in student_heights:
#   total += i
#   students +=1
# average = round(total/students) 
# print(f"total height = {total}")
# print(f"number of students = {students}")
# print(f"average height = {average}")


# # Input a list of student scores
# student_scores = input().split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# max = 0
# for i in student_scores:
#   if max < i:
#     max = i
#   else:
#     max = max

# print(f"The highest score in the class is: {max}")

# # for loop with range

# for i in range(0,10,3):
#     if i %2 == 0:
#         print(f"{i} is even number")

#     else:
#         print(f"{i} is odd number")

# sum = 0 
# for i in range(1,101):
#     sum +=i

# print(sum)
    

# FizzBuzz game
# Write your code her
for i in range (1,101):
  if i%3 == 0 and i%5==0:
    print("FizzBuzz")
  elif i %3 == 0:
    print("Fizz")
  elif i%5 == 0:
    print("Buzz")

  else:
    print(i)
  

# # py password generator
# import random

# print("Welcome to the PyPassword Generator!")
# # Generating both uppercase and lowercase alphabets in one list
# alphabets = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
# symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '_', '+', '-', '=', '<', '>', '?', '/']
# numbers = [str(i) for i in range(0,10)]


# al = int(input("How many aphabates you want in your password?\n"))
# sym = int(input("How many symbols you want in your password?\n"))
# num = int(input("How many numbers you want in your password?\n"))
# pall=''
# for i in range(al):
#   pall += random.choice(alphabets)
# for x in range(sym):
#   pall += random.choice(symbols)
# for j in range(num):
#   pall += random.choice(numbers)
# print(f"Your random password is: {pall}")



import random

print("Welcome to the PyPassword Generator!")

alphabets = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '_', '+', '-', '=', '<', '>', '?', '/']
numbers = [str(i) for i in range(0, 10)]  # Convert each number to a string

al = int(input("How many alphabets do you want in your password?\n"))
sym = int(input("How many symbols do you want in your password?\n"))
num = int(input("How many numbers do you want in your password?\n"))

password = ''

for _ in range(al):
    password += random.choice(alphabets)

for _ in range(sym):
    password += random.choice(symbols)

for _ in range(num):
    password += random.choice(numbers)

# Shuffle the password to make it more random
password_list = list(password)
random.shuffle(password_list)
final_password = ''.join(password_list)

print(f"Your random password is: {final_password}")



