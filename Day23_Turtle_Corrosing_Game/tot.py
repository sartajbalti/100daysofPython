from turtle import Turtle

class Tot(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('green')
        self.setheading(90)
        self.penup()
        self.goto(0,-280)

    def up(self):
        self.penup()
        self.forward(10)