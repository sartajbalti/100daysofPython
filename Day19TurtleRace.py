# Event Listner
# turtle
from turtle import Turtle, Screen, TK
# t = Turtle()
def move_f():
    t.forward(10)
def move_b():
    t.backward(10)
    
def counter_c():
    t.left(10)
def clock_c():
    t.right(10)
def clear_d():
    t.clear()
    t.penup()
    t.goto(0,0)
    t.pendown()
    
# object state

import random
screen = Screen()
screen.setup(width=500,height=400)
screen.title("Turtle Race")
user_bet = screen.textinput(title="Make your bet",prompt="Which color will win?")
colors = ["red","orange","yellow","green","blue","purple"]


y = -130
is_race = False
all_turtle = []
for color_name in colors:
    # Create a turtle with the given color
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color_name)

    # Set the initial position and increment y
    new_turtle.penup()
    new_turtle.goto(-200, y)
    y += 50
    all_turtle.append(new_turtle)
    # movement from random o to 10
if user_bet:
     is_race = True
while  is_race:
    
    for turtle in all_turtle:
        if turtle.xcor()>215:
            wining_turtle = turtle.pencolor()
            if wining_turtle == user_bet:
                print("You won!")
                TK.messagebox.showinfo(title="Result", message="You Won!")
                is_race = False
            else:
                print(f"Sorry, you lost. The wining turtle is {wining_turtle}")
                TK.messagebox.showinfo(title="Result", message=f"Sorry, you lost. The wining turtle is {wining_turtle}")
                is_race = False
            
        random_dis = random.randint(0,10)
        turtle.forward(random_dis)
        
    
    # control the turtles
  
# tom =Turtle(shape='turtle')
# tom.penup()
# tom.goto(-200,-50)
# tem =Turtle(shape='turtle')
# tem.penup()
# tem.goto(-200,0)
# tam =Turtle(shape='turtle')
# tam.penup()
# tam.goto(-200,50)
# tom =Turtle(shape='turtle')
# tom.penup()
# tom.goto(-200,100)


# screen.listen()
# screen.onkey(key="a",fun=counter_c)
# screen.onkey(key="w",fun=move_f)
# screen.onkey(key="s",fun=move_b)
# screen.onkey(key="d",fun=clock_c)
# screen.onkey(key="c",fun=clear_d)
screen.exitonclick()