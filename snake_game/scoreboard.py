from turtle import Turtle

data_loc = "/home/Mokshit/Documents/Programming_files/Python/Programs/Projects/snake_game/snake_data.txt"
ALIGNMENT = 'center'
FONT = ('Courier', 16, 'normal')

with open(data_loc, 'r') as f:
    score = f.read()

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(score)
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.hideturtle()

    def update_score(self):
        self.score += 1
        self.print_score()
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(data_loc, mode='w') as f:
                f.write(f"{self.high_score}")
        self.score = 0
        self.print_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", move=False,
    #                align=ALIGNMENT, font=FONT)

    def print_score(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", move=False,
                   align=ALIGNMENT, font=FONT)
