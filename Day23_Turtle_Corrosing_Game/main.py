from turtle import Screen, Turtle
from tot import Tot
from cars import Cars
from score import Scoreboard
screen = Screen()
screen.setup(600,600)
screen.tracer(0)
tot = Tot()
car = Cars()
score = Scoreboard()
import time
# cars_moved = 0  
game_on = True
while game_on:
    time.sleep(0.1)
    car.create_cars()
    car.move_car()
    # cars_moved+=1
    screen.update()
    for c in car.car_list:
        if tot.distance(c) < 20:  # Adjust the distance as needed
            game_on = False
            score.game_over()
        
    if tot.ycor() > 280:  # Adjust the y-coordinate as needed
        tot.goto(0,-280)
        car.level_up()
        score.increase()
    # if cars_moved >= 100:
    #     car.create_cars(5)  # Create additional cars
    #     cars_moved = 0 

    screen.listen()
    screen.onkey(tot.up, 'Up')
    screen.listen()
    screen.onkey(tot.up,'Up')

screen.exitonclick()

    

