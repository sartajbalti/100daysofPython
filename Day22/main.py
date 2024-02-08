# Pong Game
# creat screen , creat move a paddle creat another padle creat the bal and move , detect collision withwall and bounce
# detect cllision with paddle 
# detect when paddle misses 
# keep score
from turtle import Turtle, Screen
from paddle import Paddle
from breakline import Breakline
from ball import Ball
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
breakline = Breakline()
paddle = Paddle((350,0))
paddle1= Paddle((-350,0))
ball = Ball()
score_left = 0
score_right = 0

# Create score display for both players
score_display_left = Turtle()
score_display_left.hideturtle()
score_display_left.penup()
score_display_left.color('white')
score_display_left.goto(-100, 250)
score_display_left.write(f"Player 1: {score_left}", align="center", font=("Courier", 24, "normal"))

score_display_right = Turtle()
score_display_right.hideturtle()
score_display_right.penup()
score_display_right.color('white')
score_display_right.goto(100, 250)
score_display_right.write(f"Player 2: {score_right}", align="center", font=("Courier", 24, "normal"))

# Function to update score display
def update_score():
    score_display_left.clear()
    score_display_left.write(f"Player 1: {score_left}", align="center", font=("Courier", 24, "normal"))
    score_display_right.clear()
    score_display_right.write(f"Player 2: {score_right}", align="center", font=("Courier", 24, "normal"))

# Function to handle ball miss
def handle_miss():
    global score_left, score_right
    if ball.xcor() > 390:
        score_left += 1
    elif ball.xcor() < -390:
        score_right += 1
    update_score()
    ball.reset_position()

# Listen for paddle movements
screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")
screen.onkey(paddle1.up, "w")
screen.onkey(paddle1.down, "s")

# Main game loop
game_on = True
while game_on:
    screen.update()
    ball.move()

    # Check for paddle collision
    if (paddle.distance(ball) < 50 and ball.xcor() > 330) or (paddle1.distance(ball) < 50 and ball.xcor() < -330):
        ball.bounce_x()

    # Check for wall collision
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Check if the ball misses a paddle
    if ball.xcor() > 390 or ball.xcor() < -390:
        handle_miss()

screen.exitonclick()