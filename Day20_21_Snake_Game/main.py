# main.py

from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
scoreboard = Scoreboard()
# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create the food
food = Food()

# Create the snake
snake = Snake(food)

# Create the scoreboard


# Listen for key events
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main game loop
game_on = True
while game_on:
    screen.update()
    time.sleep(.2)
    snake.move()

    # Check for collision with food
    if snake.check_collision_with_food():
        snake.eat_food()  # Increase snake length and update score
        scoreboard.clear()
        scoreboard.write(f"Score: {snake.score}", align="center", font=("Courier", 24, "normal"))

    # Check for collision with walls
    if snake.check_collision_with_wall():
        game_on = False
        scoreboard.clear()
        scoreboard.goto(0, 0)
        scoreboard.write(f"Game Over! Final Score: {snake.score}", align="center", font=("Courier", 24, "normal"))

    if snake.check_collision_with_snake():
        game_on = False
        scoreboard.clear()
        scoreboard.goto(0, 0)
        scoreboard.write(f"Game Over! Final Score: {snake.score}", align="center", font=("Courier", 24, "normal"))

screen.exitonclick()
