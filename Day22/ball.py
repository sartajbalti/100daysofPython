from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()  # Lift pen to prevent drawing while moving
        self.x_speed = 2  # Initial x-axis speed
        self.y_speed = 2  # Initial y-axis speed

    def move(self):
        new_x = self.xcor() + self.x_speed
        new_y = self.ycor() + self.y_speed
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_speed *= -1

    def bounce_x(self):
        self.x_speed *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
