# Turtle graphics
from turtle import*
import random
timmy = Turtle()
# timmy.shape('turtle')
timmy.color('orange')
# tom = Turtle()
# # tom.color("blue")
def set_random_color():
    # Generate random values for RGB (Red, Green, Blue)
    red = random.random()
    green = random.random()
    blue = random.random()

    # Set the turtle's color
    r = (red, green, blue)
    return r
colors = ['orange', 'purple','blue','yellow','red','pink','brown','wheat','SeaGreen','DeepSkyBlue','IndianRed']
# for i in range(3,11):
#     angle = 360/i
#     timmy.color(random.choice(colors))
#     for _ in range(i):
#         timmy.forward(100)
#         timmy.right(angle)

# for _ in range(4):
#     # tom.right(90)
#     # tom.forward(100)
#     timmy.forward(100)
#     timmy.right(90)

# tick = Turtle()
# tick.shape('circle')
# tick.color('green')
# tick.left(90)
# for _ in range(15):
    
#     tick.forward(10)
#     tick.penup()
#     tick.forward(10)
#     tick.pendown()
# timmy.forward(100)
# for _ in range(3):
#     timmy.color('blue')
    
#     timmy.right(120)
#     timmy.forward(100)
# timmy.color('black')   
# for i in range(5):
#     timmy.right(72)
#     timmy.forward(100)
   
# # t = Turtle()
# # # hexagone
# timmy.color('brown')
# for _ in range(6):
#     timmy.right(360/6)
#     timmy.forward(100)
# timmy.color('purple')
# for _ in range(7):
    
#     timmy.right(360/7)
#     timmy.forward(100)
# timmy.color('red')
# for _ in range(8):
    
#     timmy.right(360/8)
#     timmy.forward(100)
# timmy.color('pink')
# for _ in range(9):
#     timmy.right(360/9)
#     timmy.forward(100)
# timmy.color('yellow')
# for _ in range(10):
#     timmy.right(36)
#     timmy.forward(100)
    
# for _ in range (11):
#     timmy.right(360/11)
#     timmy.forward(100)

timmy.pensize(2)
timmy.speed(0)
# timmy.forward(100)
direc = [0,90,180,270]
# for _ in range(300):
#     # timmy.color(random.choice(colors))
#     timmy.color(set_random_color())
#     # choice = random.randint(50,100)
#     angle = random.choice(direc)
#     timmy.forward(30)
#     timmy.setheading(angle)

for _ in range(36):
    timmy.color(set_random_color())
    timmy.circle(100)
    timmy.left(10)
screen = Screen()
screen.exitonclick()