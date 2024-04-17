from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)
        # x_cor = self.xcor()
        # y_cor = self.ycor() + MOVE_DISTANCE
        # self.goto(x_cor, y_cor)
    
    def new_level(self):
        self.goto(STARTING_POSITION) 




