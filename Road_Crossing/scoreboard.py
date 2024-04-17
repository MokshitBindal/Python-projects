from turtle import Turtle
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(-200,250)
        self.hideturtle()
        self.level = 1
        self.print_score()
    
    def print_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align = "center", font= FONT)
    
    def increase_level(self):
        self.level += 1

    def lost(self):
        self.goto(0,0)
        self.write("GAME OVER", align = "center", font= FONT)
