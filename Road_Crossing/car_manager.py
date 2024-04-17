import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []

    def new_car(self):
        if random.randint(0,5) == 1:
            car = Turtle("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.goto(300, random.randint(-250, 250))
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.backward(MOVE_INCREMENT)
        # # for car in range(len(self.cars)):
        # #     y_cor = self.cars[car].ycor()
        # #     self.cars[car].goto(-280, y_cor)
        # #     # self.cars[car].hideturtle()
        # if self.xcor() > -280:
        #     y_cor = self.ycor()
        #     x_cor = self.xcor() - MOVE_INCREMENT
        #     self.goto(x_cor, y_cor)
        
        # # else:
        # #     self.hideturtle()


