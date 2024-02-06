from turtle import Turtle, Screen
starting_position =[(0,0),(-20,0),(-40,0)]
move_dist = 20
up = 90
down = 270
left = 180
right = 0
class Snake:
    def __init__(self):
        
        self.snakes =[]
        self.create_snake()
    def create_snake(self):
        for position in starting_position:
            self.snake = Turtle(shape='square')
            self.snake.color('white')
            self.snake.penup()
            self.snake.goto(position)
            self.snakes.append(self.snake)

    def move(self):
        for snake_no in range(len(self.snakes)-1, 0,-1):
            new_x = self.snakes[snake_no-1].xcor()
            new_y = self.snakes[snake_no-1].ycor()
            self.snakes[snake_no].goto(new_x,new_y)
        self.snakes[0].forward(move_dist)

    def up(self):
        if self.snakes[0].heading() !=down:
            self.snakes[0].setheading(up)

    def down(self):
        if self.snakes[0].heading()!= up:
            self.snakes[0].setheading(down)

    def left(self):
        if self.snakes[0].heading()!= right:
            self.snakes[0].setheading(left)
    def right(self):
        if self.snakes[0].heading()!= left:
            self.snakes[0].setheading(right)

    def collision(self):
        if self.snakes[0].xcor() >290 or self.snakes[0].xcor()<-290 or self.snakes[0].ycor()>290 or self.snakes[0].ycor()<-290:
            return True
        else:
            return False
        

