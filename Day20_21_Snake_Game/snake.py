# snake.py

from turtle import Turtle
import random

MOVE_DISTANCE = 20

class Snake:
    def __init__(self, food):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]
        self.food = food
        self.score = 0

    def create_snake(self):
        for position in [(0, 0), (-20, 0), (-40, 0)]:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.snakes.append(segment)

    def move(self):
        for seg_num in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[seg_num - 1].xcor()
            new_y = self.snakes[seg_num - 1].ycor()
            self.snakes[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def check_collision_with_food(self):
        return self.head.distance(self.food) < 15

    def eat_food(self):
        self.score += 1
        self.food.refresh()
        self.add_segment(self.snakes[-1].position())

    def check_collision_with_wall(self):
        x = self.head.xcor()
        y = self.head.ycor()
        if abs(x) >= 290 or abs(y) >= 290:
            return True
        return False
    def check_collision_with_snake(self):
        for segment in self.snakes[1:]:
            if self.head.distance(segment) < 10:  # Adjust this value as needed
                return True
        return False
    


