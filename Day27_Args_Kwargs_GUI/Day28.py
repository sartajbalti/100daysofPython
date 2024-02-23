# Building pomodoro technique
from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text=f"00:00")
    label.config(text="Timer")
    check.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_s = WORK_MIN*60
    sbreak_s = SHORT_BREAK_MIN*60
    lbreak_s = LONG_BREAK_MIN*60
    if reps % 8==0:
        label.config(text="Break",fg=RED)
        
        countdown_timer(lbreak_s)
    if reps%2==0:
        countdown_timer(sbreak_s)
        label.config(text="Break", fg=PINK)
    else:
        countdown_timer(work_s)
       

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown_timer(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_min < 10:
        count_min=f"0{count_min}"
    if count_sec < 10:
        count_sec= f"0{count_sec}"
    
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000,countdown_timer,count-1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks+="✓"
        check.config(text=marks,font=(FONT_NAME,20,"bold"))
    
    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

label = Label(text="Timer",font=(FONT_NAME,35,"bold"),fg=GREEN,bg=YELLOW)
label.grid(column=1,row=0)
# Canvas Widget
canvas = Canvas(window, width=200, height=224,bg=YELLOW, highlightthickness=0)
image =PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=image)
timer_text = canvas.create_text(100,130,text="00:00",font=(FONT_NAME,35,"bold"),fill="white")
canvas.grid(column=1,row=1)  # Spanning across 3 columns

# Start Button
start_button = Button(text="Start", highlightthickness=0,command=start_timer)
start_button.grid(column=0, row=2)  # Increased padding on both sides

# Reset Button
reset_button = Button(text="Reset", highlightthickness=0,command=reset)
reset_button.grid(column=2, row=2)  # Increased padding on both sides

check = Label(fg=GREEN,bg=YELLOW)
check.grid(column=1,row=3)


window.mainloop()