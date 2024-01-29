# Debugging 
# finding the error in the code is debugging 
# Tips and techniques to find out the bug 
#  # Describe Problem 
def my_function():
    '''The reason of not getting an out put is the range is from 1 to 20 so it include 1 and exclude 20,
    that means i is never become equall to 20'''
    for i in range(1,20):
        if i == 20:
            print("You got 20")
my_function()

# # Reproduce the Bug 
# from random import randint
# dice_imgs = ["1","2","3","4","5"]
# dice_num = randint(1,6)
# # fix 
# # dice_num = randint(0,5)
# '''reason of getting the index out of range is the dice num is 6 when it pass to images it will take the 7th element,
# which is not in dice Images so it won't print'''
# print(dice_imgs[dice_num])

# Act computer 
# year = int(input("What's your year of birth?"))
# if year>=1980 and year <=1994:
#     print("You are a millenial")

# elif year>1994:
#     print("You are a Gen Z.")

# # Fix bug 
# age = input("Whats your age? ")
# if age>18:
#     print("You can drive at the age of {age}")

# # Use print for debugging also 
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# print(f"No of words per page {word_per_page}")
# total_words = pages * word_per_page
# print(total_words)

# Use Debugger 
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item*2
    b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])

# Debugging tips
# - Take a Break 
# - Ask a Friend
# - Run the code often
# - Ask stackOverflow 
# - Ask ChatGpt
 