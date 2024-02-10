from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}",align='left', font=("Arial", 24, "bold"))
    def increase(self):
        self.level+=1
        self.update_score()
    def game_over(self):
      self.goto(0,0)
      self.write("Game Over!", align="center", font=("Arial", 64, "bold"))