from turtle import Turtle
import random
colors = ['red', 'yellow', 'green', 'blue']
start_move=5
class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_list = []
        self.car_speed=5

    def create_cars(self):
        chance =random.randint(1,6)
        if chance==1:
            color = random.choice(colors)
            x = 260  # Adjust as needed for proper positioning
            y = random.randint(-250,250)  # Keep cars within screen boundaries
            car = Turtle()  # Create a new car instance
            car.penup()
            car.shape('square')
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(color)
            car.goto(x, y)
            car.setheading(180)  # Point cars to the left
            self.car_list.append(car)

    def move_car(self):
        for car in self.car_list:
            car.forward(self.car_speed)
    def level_up(self):
        self.car_speed+=10


    
    