from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.setposition(position)

    def up(self):
        if self.ycor() < 250:  # Adjust as needed based on your screen size
            self.sety(self.ycor() + 20)

    def down(self):
        if self.ycor() > -240:  # Adjust as needed based on your screen size
            self.sety(self.ycor() - 20)