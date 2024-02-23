# GUI using tkinter
# creating a new GUI using tkinter
# Advance funtions of Advanced functions Default arguments Args and  Kwargs

# Finally we will make Unit conversions mile to km using these ideas 

# 1: GUI and Intro to Tkinter 
# crating windows and buttons using tkinter
import tkinter

window = tkinter.Tk()
window.title("Mile to km Converter")
# window.minsize(500,300)
window.config(padx=20, pady=20)

input = tkinter.Entry()
input.grid(column=1,row=0)

text = tkinter.Label(text="Miles", font=('Arial', 16))
text.grid(column=2,row=0)
text1 = tkinter.Label(text="is equal to", font=('Arial', 14),fg='blue')
text1.grid(column=0, row=1)

text2 = tkinter.Label(text="Km", font=('Arial', 16))
text2.grid(column=2, row=1)

result = tkinter.Label(text=0, font=('Arial', 16))
result.grid(column=1, row=1)
def calculate():
    value = float(input.get())
    # miles to km
    kms = value*1.609
    result_value = round(float(kms), 2)
    result.config(text=f"{result_value}")
    
    
button = tkinter.Button(text="Calculate", font=('Arial', 18),command=calculate)
button.grid(column=1, row=2)





# # Advance python arguments 
# # Unlimited arguments 
# def add (*args):
#     sum = 0
#     for n in args:
#         sum+=n
#     print(sum)
    
# # Kwargs  

# def calculates(n,**kwargs):
#     print(kwargs)
#     print(kwargs['add'])
#     n+=kwargs['add']
#     n*=kwargs['multiply']
#     print(n)
    
# calculates(2,add=3,multiply=5)
# add(1,2,3,4,5)








window.mainloop()

