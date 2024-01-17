# # Functions with inputs 
# import random
# words =["sartaj","skardu"]
# choice = random.choice(words)
# l = []
# for i in choice:
#     l.append('_')
# print(*l)
# live = 6
# end_game = False
# while not end_game:
#     a = input("Guess the character: ")
#     for i in range(0,len(choice)):
#         b = choice[i]
#         if a == b:
#             l[i]=a
#     print(*l)
#     if a not in choice:
#         live-=1
#         print("you guess is wrong try again")
#         if live==0:
#             end_game =True
#             print("You Loose")
#     if "_" not in l:
#         end_game = True
#         print("You Won")

#  caesar cipher
# arguments and parameters
# Functions
import random
# def greet(a):
#     print(f"Hello {a}")
# word = ["Sartaj","JJ","Han","Zhang"]
# a = random.choice(word)
# greet(a)

# Positional vs Key Arguments
# Functions with more inputs
def greet_with(a,b,c):
    print(f"{a} lives in {b}")
    # just for am example not real bmi 
    print(f"His BMI is {c*12}")
# a = input("Enter the name: ")
# b =input("Enter the location: ")
# c = int(input("Enter his height: "))

# greet_with(a = "Sartaj",b="Stak",c=12)
# def greet_with(a,b,c):
#     print(f"{a} lives in {b}")
#     # just for am example not real bmi 
#     print(f"His BMI is {c*12}")
# x = input("Enter the name: ")
# y =input("Enter the location: ")
# z = int(input("Enter his height: "))

# greet_with(x,y,z)



# num = 11
# # If given number is greater than 1

#     # Iterate from 2 to n / 2
# for i in range(2, num):
#     # If num is divisible by any number between
#     # 2 and n / 2, it is not prime
#     if (num % i) == 0:
#         print(num, "is not a prime number")
#         break
# else:
#     print(num, "is a prime number")

# Caesar Cipher
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z']
def cispher(text,shift,direction):
    end_text=""
    for i in text:
        if i in alphabet:
            position = alphabet.index(i)
            if cispher =="decode":
                shift*=-1
            new_p = position + shift
            if new_p > len(alphabet):
                new_p = new_p-len(alphabet)
            end_text+=alphabet[new_p]
        else:
            end_text+=i

    print(f"{direction}d text is {end_text}")

should_countinue = True
while should_countinue:
    direction =input("Type 'encode' to encrypt and 'decode' to decrypt: ").lower()
    text = input("Enter the message: \n").lower()
    shift = int(input("Type the shift number:\n"))  
    shift= shift%26
    cispher(text,shift,direction)
    result = input("Type 'yes' if you want to continue else 'no' to end: ").lower()
    if result =='no':
        print("Good Bye..")
        should_countinue=False




# if direction=="decode":
#     ct = ""
#     for i in text:
#         position = alphabet.index(i)
#         np = position-shift
#         nl = alphabet[np]
#         ct+=nl
#     print(f"Your derypted message is {ct}")

# elif direction == "encode":
#     cipher_text =""
#     for i in text:
#         position = alphabet.index(i)
#         new_p = position + shift
#         if new_p > len(alphabet):
#             new_p = new_p-len(alphabet)
#         new_l = alphabet[new_p]
#         cipher_text+=new_l
#     print(f"the encrypted text is {cipher_text}")
# else:
#     print("Please enter the correct direction")
# def decrypt(text,shift):
#     ct = ""
#     for i in text:
#         position = alphabet.index(i)
#         np = position-shift
#         nl = alphabet[np]
#         ct+=nl
#     print(f"Your derypted message is {ct}")
# def encrypt(text, shift):
#     cipher_text =""
#     for i in text:
#         position = alphabet.index(i)
#         new_p = position + shift
#         if new_p > len(alphabet):
#             new_p = new_p-len(alphabet)
#         new_l = alphabet[new_p]
#         cipher_text+=new_l
#     print(f"the encrypted text is {cipher_text}")
# if direction=="encode":
#     text = input("Enter the message to encrypt: \n").lower()
#     shift = int(input("Type the shift number:\n"))
#     encrypt(text,shift)
# elif direction == "decode":
#     text = input("Enter the message to decrypt: \n").lower()
#     shift = int(input("Type the shift number:\n"))


#     decrypt(text,shift)
# else:
#     print("Please enter the correct direction")