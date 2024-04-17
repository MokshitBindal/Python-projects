import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

car_speed = 1

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_man = CarManager()
# car.move()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1/car_speed)
    # time.sleep(0.2)
    screen.update()

    car_man.new_car()
    car_man.move()

    # check for collision
    for car in car_man.all_cars:
        if player.distance(car) < 20:
            scoreboard.lost()
            game_is_on = False


    # Detect if the player reached the finish point
    if player.ycor() >= 280:
        player.new_level()
        # Increase the player's level
        scoreboard.increase_level()
        scoreboard.print_score()

        # Increase the Car speed
        # if car_speed <= 10:
        #     car_speed += 1
        car_speed += 1


    


screen.exitonclick()