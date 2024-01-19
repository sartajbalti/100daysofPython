# # Dictionaries and Nesting
# # Nesting list in list and Dic in Dic

# # Dictionaries 
# # have two parts key and values
# program_dict = {"Bug":"An error in a program that prevenets the program from running.",
#                 "Funtion":"A piece of code that you can easily call over and over again."}

# print(program_dict["Bug"])
# #  adding new entry 
# program_dict["Loop"] = "The action of doing something over and over again."
# # print(program_dict)
# # add in empty dic 
# # empty_dict = {}
# # # wipe an existing dic 
# # program_dict = empty_dict

# # print(program_dict)

# # edit an item in dic 
# program_dict["Bug"] = "An error"

# # print(program_dict)

# # Loop through the dic 
# for  key in program_dict:
#     print(key)
#     print(program_dict[key])

# # Nesting 
# sample_dic = {"Country":["France","Pakistan","Japan"],"Capital":["Paris","Islamabad","Tokyo"]}

# # dic in dic

# sam_dic = {"Country":{"France":"2 cities","Pakistan":"three cities","Japan":"4 cities"},"Visits":{"Paris":"once","Islamabad":"twice","Tokyo":"many times"}}
# for key in sam_dic:
#     for a in sam_dic[key]:
#         print(a)
#         print(sam_dic[key][a])
    
# country = input() # Add country name
# visits = int(input()) # Number of visits
# list_of_cities = eval(input()) # create list from formatted string

# travel_log = [
#   {
#     "country": "France",
#     "visits": 12,
#     "cities": ["Paris", "Lille", "Dijon"]
#   },
#   {
#     "country": "Germany",
#     "visits": 5,
#     "cities": ["Berlin", "Hamburg", "Stuttgart"]
#   },
# ]
# # Do NOT change the code above 👆

# # TODO: Write the function that will allow new countries
# # to be added to the travel_log. 

# def add_new_country(country,visits,list_of_cities):
#   new_data = {"country":country,"visits":visits,"cities":list_of_cities}
#   travel_log.append(new_data)
# # Do not change the code below 👇
# add_new_country(country, visits, list_of_cities)
# print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
# print(f"My favourite city was {travel_log[2]['cities'][0]}.")
import os
print("Welcome to the silent bit")
end_bit = False
dic = {}
def find_highest (bidding):
    heighest_bit = 0
    for key in bidding:
        amount = bidding[key]
        if amount>heighest_bit:
            heighest_bit=amount
            winer = key

    print(f"The winer is {winer} with a bit of {heighest_bit}$")

while not end_bit:
    name = input("What is your name? \n")
    bit = int(input("What is your bit in $:\n"))
  
    dic[name] = bit
    a = input("Is there any other onw who wants to bit? yes or no : \n").lower()

    if a =="no":
        find_highest(dic)
        end_bit=True
    elif a == "yes":
        os.system('clear')

    
