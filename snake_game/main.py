from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import ScoreBoard

# https://docs.python.org/3/library/turtle.html# 

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
snake_speed=1

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


board = ScoreBoard()
board.print_score()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.14/snake_speed)
    snake.move()
    # detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        board.update_score()
        snake_speed+=0.2
    
    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        board.reset()
        snake.reset()
        snake_speed = 1
        # is_game_on = False
        # board.game_over()
    
    #detect collision with itself
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            board.reset()
            snake.reset()
            snake_speed = 1
            # is_game_on = False
            # board.game_over()

screen.exitonclick()
