import colorgram
from turtle import Turtle, Screen
timmy = Turtle()
img = "images.jpg"
pallete = colorgram.extract(img, 30)

colors_list = [(color.rgb.r/255, color.rgb.g/255, color.rgb.b/255) for color in pallete]
start_x = -200
start_y = 200

# Dot size and gap
dot_size = 20
gap = 50

# Loop through rows
for row in range(10):
    # Move to the start of the row
    timmy.penup()
    timmy.goto(start_x, start_y - row * gap)

    # Loop through columns
    for col in range(10):
        # Draw a dot
        random_color = random.choice(colors_list)
        timmy.color(random_color)
        timmy.dot(dot_size)
        timmy.penup()
        timmy.forward(gap)
screen = Screen()
screen.exitonclick()