from turtle import Turtle
from snake import Snake
# from food import Food
# food = Food()
# snake = Snake(food)
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"Score: {0}", align="center", font=("Courier", 24, "normal"))