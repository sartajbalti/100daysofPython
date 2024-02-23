from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    alphabets = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '_', '+', '-', '=', '<', '>', '?', '/']
    numbers = [str(i) for i in range(0, 10)]  # Convert each number to a string



    password = []
    al = [choice(alphabets) for _ in range(randint(8,10))]
    sy = [choice(symbols) for _ in range(randint(2,4))]
    num =[choice(numbers) for _ in range(randint(2,4))]

    total_chars = al + sy + num



    shuffle(total_chars)
    final_password = ''.join(total_chars)
    passform.insert(0, final_password)
    pyperclip.copy(final_password)
    



    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = form1.get()
    username= userform.get()
    password = passform.get()
    if len(website)==0 or len(username)==0 or len(password)==0:
        messagebox.showerror("Error", "Please fill out all fields.")
    else:
        is_ok =messagebox.askokcancel(title=website, message=f"These are the deatails entered: Email: {username}\n Password: {password}\n is it okay to save ")

        if is_ok:
            with open("./Day29_Pass_man_saver/password.txt", "a") as f:
                f.write(f"Website: {website} | Username: {username} | Password: {password}\n")
                messagebox.showinfo(title=None,message="Password Saved Successfully!")
                
            form1.delete(0,END)
            passform.delete(0,END)
            userform.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)


canvas = Canvas(window, width=200, height=200, highlightthickness=0)
image = PhotoImage(file='./Day29_Pass_man_saver/logo.png')
canvas.create_image(100,100, image=image)
canvas.grid(row=0,column=1)

# Labels
web = Label(text="Website:")
web.grid(row=1,column=0)

user = Label(text="Email/Username:")
user.grid(row=2,column=0)
password = Label(text="Password:")
password.grid(row=3,column=0)

# Forms
form1 = Entry(width=35)
form1.grid(row=1,column=1,columnspan=2)
form1.focus()
userform = Entry(width=35)
userform.grid(row=2,column=1,columnspan=2)
userform.insert(0,"sartajbalti@gmail.com")  # Default Value for Username Field
passform = Entry(show="*",width=21)
passform.grid(row=3,column=1)

# Buttons
pasbut = Button(text="Generate Password",command=password_generator)
pasbut.grid(row=3,column=2)
button = Button(text="Add",width=36,command=save_password)
button.grid(row=4,column=1,columnspan=2)
window.mainloop()



