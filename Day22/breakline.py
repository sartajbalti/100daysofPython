from turtle import Turtle
class Breakline(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)  # Set the fastest drawing speed
        self.color('white')
        self.shapesize(stretch_wid=6,stretch_len=6)

        # Move the turtle to the starting position
        self.penup()
        self.goto(0, -300)
        self.setheading(90)  # Set the turtle's orientation to face upwards

        # Define the parameters for the dashed line
        dash_length = 10  # Length of each dash
        gap_length = 5    # Length of each gap between dashes
        num_dashes = 50   # Total number of dashes

        # Draw the dashed line
        for _ in range(num_dashes):
            self.pendown()
            self.forward(dash_length)
            self.penup()
            self.forward(gap_length)

        # Hide the turtle and display the result
        self.hideturtle()