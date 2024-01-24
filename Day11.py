# # Black jack Game 

# # 
import random
import os
# cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
# end_game = False
# user = []
# computer = []
# def deal_card(a):

#     if a in cards:
#         user.append(a)
#         return user
#     elif a not in cards:
#         return "select the correct number"
# computer_choice = random.choice(cards)
# def sum_list(u):
#     sum = 0
#     for a in u:
#         sum +=a
#     return sum
        
# for i in range(1,4):
          
#     print(deal_card(int(input("Enter the number"))))
#     print(f"You selected your {i} card.") 
    
#     computer.append(computer_choice)
#     print(f"Computer first card is: {computer[0]}")

#     if i >= 2:
#         x = input("Want to select the third card? if yes type 'y' if no type 'n'")
#         if x == "n":
#             if sum_list(user)>21 or sum_list(user)<17 and sum_list(computer)<21 or sum_list(computer)>17:
#                 print(f"Your sum is {sum_list(user)} and Computer sum is {sum_list(computer)} \n You Loose ")
#             elif sum_list(computer)>21 or sum_list(computer)<17 and sum_list(user)<21 or sum_list(user)>17:
#                 print(f"Your sum is {sum_list(user)} and Computer sum is {sum_list(computer)} \n You Wins ")

#             elif sum_list(user)<sum_list(computer):
#                 print(f"Your sum is {sum_list(user)} and Computer sum is {sum_list(computer)} \n You Loose ")
#             elif sum_list(user)==sum_list(computer):
#                 print(f"Your sum is {sum_list(user)} and Computer sum is {sum_list(computer)} \n Its a tie ")
#             else:
#                 print(f"Your sum is {sum_list(user)} and Computer sum is {sum_list(computer)} \n You Wins ")
#             break
#         else:
#             continue

def deal_card():
    """Return random card from the deck"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card
def calculate_score(u):
    if sum(u)==21 and len(u)==2:
        return 0
    if 11 in u and sum(u)>21:
        u.remove(11)
        u.append(1)
    return sum(u)
def compare(user_score,computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score ==0:
        return "Lose, apponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over, You Lose"
    elif computer_score >21:
        return "Opponent went over, You win"
    elif user_score>computer_score:
        return "You win"
    else:
        return "You lose"
    
def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, Current Score: {user_score}")
        print(f"Computer First Card: {computer_cards[0]}")
        if user_score == 0 or computer_score==0 or user_score>21:
            is_game_over = True
        else:
            new = input("Want to draw another card? if yes type 'y' else 'n'")
            if new =='y':
                user_cards.append(deal_card())
                
            else:
                is_game_over=True

    """Computers stategy for cards selection"""
    while computer_score !=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score =calculate_score(computer_cards)
        print(f"Your Final cards: {user_cards}, Final Score: {user_score}")
        print(f"Computer Final Cards: {computer_cards}, Final Score: {computer_score}")
    print(compare(user_score,computer_score))
while input("Do you want to play the game? type 'y' to play again else 'n'")=="y":
    os.system('clear')
    play_game()









