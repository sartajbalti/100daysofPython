# Heigher or Lower searches 
# game 

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

from Day14.gamedata import data
import random
import os
def account_details(account):
    account_name = account['name']
    account_dec = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_dec}, from {account_country}"

def check_answer(guess,a_followers,b_followers):
    if a_followers>b_followers:
        return guess =="a"
    else:
        return guess =="b"

game_should_continue = False
print(logo)
score = 0
account_b = random.choice(data)
while not game_should_continue:
    
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)


    print(f"Compare A: {account_details(account_a)}")
    print(vs)
    print(f"Againts B: {account_details(account_b)}")
    guess = input("Who has more Followers? Type 'A' or 'B': ").lower()

    a_followers = account_a['follower_count']
    b_followers = account_b['follower_count']
    is_correct = check_answer(guess, a_followers,b_followers)

    os.system('clear')
    print(logo)
    if is_correct:
        score+=1
        print(f"You are right! Current Score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        again = input("Want to pay again? Type 'Yes' or 'No': ").lower()
        if again == 'no':
            game_should_continue = True
            print(f"Your sFinal score: {score}")
        
    









# end_game = False
# print(logo)
# score = 0
# while not end_game:
#     choice = random.sample(data,2)
    
#     print(f"Compare A: {choice[0]['name']}, a {choice[0]['description']}, from {choice[0]['country']}")
#     print(vs)
#     print(f"Againsts B: {choice[1]['name']}, a {choice[1]['description']}, from {choice[1]['country']}")
#     user_choice = input("Who has more Followers? Type 'A' or 'B': ").lower()
#     print(logo)
#     if user_choice == 'a':
#         if choice[0]['follower_count']>choice[1]['follower_count']:
#             score +=1
            
#             print(f"You are right! Current Score {score}")
#         else:
#             print(f"Sorry, that's wrong. Final score: {score}")
#             again = input("Want to pay again? Type 'Yes' or 'No': ").lower()
#             if again =='no':
#                 end_game = True
        
#     elif user_choice == "b":
#         if choice[1]['follower_count']>choice[0]['follower_count']:
#             score +=1
#             print(f"You are right! Current Score {score}")
#         else:
#             print(f"Sorry, that's wrong. Final score: {score}")
#             again = input("Want to pay again? Type 'Yes' or 'No': ").lower()
#             if again =='no':
#                 end_game = True
    
# score = 0
# end_game = False
# while not end_game:
#     a = random.sample(person_follower.items(),2)
#     print(f"Compare the followers of A: {a[0][0]} and B: {a[1][0]} footballers.")
#     choose = input("Which one you thinks have more followers A or B: ")
#     if choose == 'A':
#         if a[0][1]>a[1][1]:
#             print("You guess it correct..")
#             score +=1
#         else:
#             print("You are wrong")
#             end_game = True
#         print(f"Your Score is {score}")
#     elif choose == "B":
#         if a[1][1]>a[0][1]:
#             print("You guess it correct..")
#             score +=1
#         else:
#             print("You are wrong")
#             end_game = True
#         print(f"Your Score is {score}")