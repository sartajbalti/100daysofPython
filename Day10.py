# Functions with outputs 
def my_function():
    result = 3+2
    return result
output = my_function()
print(output)
def format_name(f_name,l_name):
    f_name = f_name.title()
    l_name = l_name.title()
    return f"formated name is {f_name} {l_name}"

output1= format_name("SartaJ","ahmed")
print(output1)

# return in more detail 

# #  multiple return values
# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False
  
# def days_in_month(year,month):
#   """You can write a doc string like this 
#   it take the year and month and show you the number of days and also count leep years. """
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   month_days[month-1]

#   if is_leap(year) is True:
#     month_days[1] = 29
#     a = month_days[1]
#     return a

#   else:
#     a = month_days[month-1]
#     return a
    
  
# year = int(input()) # Enter a year
# month = int(input()) # Enter a month
# days = days_in_month(year, month)
# print(days)

# Calculator 


def add(a,b):
    return a+b
def multiply(a,b):
    return a*b
def sub(a,b):
    return a-b
def devide(a,b):
    return a/b

operation = {"+":add,"-":sub,"*":multiply,"/":devide}

def calculator():    
    should_continue = True

    num1 = int(input("What is your first number? "))
    while should_continue:
        a = input("enter the operator.")
        num2 = int(input("What is the number? "))
        function = operation[a]
        answer1 = function(num1,num2)
        print(f"{num1} {a} {num2} = {answer1}")
        x = input(f"Type y to continue with {answer1}, or type 'n' to start a new calculation and type x to exit.: ")
        if  x== "y":
            num1 = answer1
        elif x =="x":
            should_continue = False
        else:
            calculator()
calculator()
    

