# # Scope 

# # e = 1
# # def inc_e():
# #     e = 2
# #     return e
# # print(f"enemies outside function: {inc_e()}")


# # # Local scope 
# # def drink():
# #     """Local scope  variable or anything can be call within the wall"""
# #     potion = 2
# #     print(potion)
# # drink()

# # Global Scope
# """variable or anything that can be access or call anywhere in the code"""
# player =10 
# def drink():
#     """Local scope a variable can be call within the function"""
#     potion = 2
#     print(player)
# drink()

# # There is no block scope in python 
# game_level = 3
# enemimes = ["Sartaj","Ahmed"]

# if game_level<4:
#     new = enemimes[0]

# print(new)


# # How to modify variables with globel scope

# # e = 1
# # def inc_e():
# #     global e
# #     e = 2
# #     print(e)
# # inc_e()
# # print(f"enemies outside function: {e}")

# e = 1
# def inc_e():
#     return e + 2

# print(f"enemies outside function: {inc_e()}")

# # Global Constants in python 

# pi = 3.14159

# """in order to get the constants global is very usefull"""
# URL = "https://sartajbalti.github.io"



# Number guessing Game!!
import random
import os
print(''' ________                               _______               ___.                   ._._._._.
 /  _____/ __ __   ____   ______ ______  \      \  __ __  _____\_ |__   ___________   | | | | |
/   \  ___|  |  \_/ __ \ /  ___//  ___/  /   |   \|  |  \/     \| __ \_/ __ \_  __ \  | | | | |
\    \_\  \  |  /\  ___/ \___ \ \___ \  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/   \|\|\|\|
 \______  /____/  \___  >____  >____  > \____|__  /____/|__|_|  /___  /\___  >__|      ________
        \/            \/     \/     \/          \/            \/    \/     \/          \/\/\/\/ ''')
conti = False
print("Welcome to the Number Guessing Game!!\n I'm thinking of a number between 1 and 100.")
difficulty_level = input("Choose a difficulty level. Type 'easy' or 'hard': ")
selected = random.randint(1,100)
while not conti:
    def level_check(no_attempts):
        for i in range(no_attempts):
            print(f"You have {no_attempts} attempts remaing to guess the number.")
            no_attempts-=1
            guess = int(input("Make a Guess: "))
            if guess == selected:
                print(f"You guessed it right {guess}")
                break
            elif guess<selected:
                print("Too Low. \n Guess again.")
            elif guess>selected:
                print("Too High. \n Guess again.")
            else:
                print("Opps outof range guess the number in range..")
            if no_attempts ==0:
                print("You run out of guesses you lose")
    if difficulty_level == 'easy':
        level_check(10)
    elif difficulty_level == 'hard':
        level_check(5)

    con = input("Want to play again?  Type 'yes' or 'no': ")
    if con =='no':
        conti = False


