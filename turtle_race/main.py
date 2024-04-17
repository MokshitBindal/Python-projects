from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet",
                            prompt="Which Turtle will win the race? Enter a colour[blue/green/cyan/red/orange/purple]: ")

colours = ["blue", "green", "purple", "red", "cyan", "orange"]
y_pos = [-150, -90, -30, 30, 90, 150]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colours[turtle_index])
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(
                    f"You've won! The {winning_color} turtle has won the race!")
            else:
                print(
                    f"You've lost! The {winning_color} turtle has won the race!")

        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)


screen.exitonclick()
