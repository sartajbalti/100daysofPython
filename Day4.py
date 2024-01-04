# 100 days of code day 4 
# Python list and randomization 

# Random Module
# Randamization is to create some random numbers generator

import random
#  generates the random integer or string or any value in the list if we want to select
# rand = random.randint(1,10)
# print(rand)
# # random float numbers between 0 to 1
# ran = random.random()
# print(ran*rand)

# # Lists
# baltistan = ["Roundu","Skardu","Khaplu","Shigar","Kharmang"]
# # balti = len(baltistan)
# # randbalti = random.randint(0,balti-1)
# # print(f"{baltistan[randbalti]} is the most beautiful region of Baltistan")

# # print(baltistan[-6])


# # Index out of range error. 
# balti_food = ["Azoq","Kulcha","prapu"]
# balti_dress = ["Nating",'Kapsha','Shalwar Qameex']

# bfd = [balti_food,balti_dress]
# print(bfd)

# line1 = ["⬜️","️⬜️","️⬜️"]
# line2 = ["⬜️","⬜️","️⬜️"]
# line3 = ["⬜️️","⬜️️","⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input() # Where do you want to put the treasure?

# letter = position[0].lower()
# alphabate = ['a','b','c']
# alphabate_index = alphabate.index(letter)
# numbe = int(position[1])-1
# map[numbe][alphabate_index]= 'X'

# print(f"{line1}\n{line2}\n{line3}")

# for i in range(len(baltistan)):
#     print(baltistan[i])

# roundu = {"center": "dambudas","bigest": "stak"}

# print(roundu['bigest'])
# b = random.choice(baltistan)
# print(b)
# print('''
#       ___________
#      '._==_==_=_.'  
#      .-\\:      /-.  
#     | (|:.     |) | 
#      '-|:.     |-'
#        \\::.    /   
#         '::. .'    
#           ) (      
#         _.' '._    
#        `"""""""`
# You win!
# ''')
rock ='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
Rock!
'''

paper ='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
Paper!
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
Scissors!
'''

print("Welcome")
print('''
  _____                            _             _____                                 
 |  __ \                          (_)           / ____|                                
 | |__) |___  __ _ _   _  ___ _ __ _  ___ __ _| |  __  __ _ _ __ ___   ___  _ __  ___ 
 |  _  // _ \/ _` | | | |/ _ \ '__| |/ __/ _` | | |_ |/ _` | '_ ` _ \ / _ \| '_ \/ __|
 | | \ \  __/ (_| | |_| |  __/ |  | | (_| (_| | |__| | (_| | | | | | | (_) | | | \__ \ 
 |_|  \_\___|\__, |\__,_|\___|_|  |_|\___\__,_|\_____|\__,_|_| |_| |_|\___/|_| |_|___/
              __/ |                                                                    
             |___/                                                                     
''')
      
user = int(input("To start the game enter 1 for Rock, 2 for Scissor and 3 for Paper.. \n"))
computer = random.randint(1,3)
if user == computer:
    if computer == 1:
          print(f"You both choose {rock}")
    elif computer == 2:
          print(f"You both choose {scissor}")
    else:
          print(f"You both choose {paper}")
          
    print("Both Choose the same its a Tie..")
    print('''
   _____          __  __ ______    ______      ________ _____  
  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ 
 | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
 | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / 
 | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ 
  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\
''')
elif user == 1:
    print(f"You choose {rock}")
    if computer == 2:
        print(f"Computer choose {scissor}")
        print('''
      ___________
     '._==_==_=_.'  
     .-\\:      /-.  
    | (|:.     |) | 
     '-|:.     |-'
       \\::.    /   
        '::. .'    
          ) (      
        _.' '._    
       `"""""""`
You win! Rock breaks the Scissor..
''')
    else:
            print(f"Computer choose {paper}")
            print('''
   _____          __  __ ______    ______      ________ _____  
  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ 
 | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
 | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / 
 | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ 
  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\
  You Loose!!!  Paper covers Rock
''' )
                  
elif user == 2:
    print(f"You both choose {scissor}")
    if computer == 3:
                  print(f"Computer choose {paper}")
                  print('''
      ___________
     '._==_==_=_.'  
     .-\\:      /-.  
    | (|:.     |) | 
     '-|:.     |-'
       \\::.    /   
        '::. .'    
          ) (      
        _.' '._    
       `"""""""`
You win! Scissor cuts the paper..
''')
    else:
            print(f"Computer choose {rock}")
            print('''
   _____          __  __ ______    ______      ________ _____  
  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ 
 | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
 | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / 
 | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ 
  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\
  You Loose!!!  Rock breaks the Scissor
''' )

elif user == 3:
    print(f"You choose {paper}")
    if computer == 1:
            print(f"Computer choose {rock}")
            print('''
      ___________
     '._==_==_=_.'  
     .-\\:      /-.  
    | (|:.     |) | 
     '-|:.     |-'
       \\::.    /   
        '::. .'    
          ) (      
        _.' '._    
       `"""""""`
You win! Paper covers Rock..
''')
    else:
        print(f"Computer choose {scissor}")
        print('''
   _____          __  __ ______    ______      ________ _____  
  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ 
 | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
 | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / 
 | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ 
  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\
  You Loose!!!  Scissor cuts the Paper.
''' )
else:
      print("You choose Invalid number..")
     

