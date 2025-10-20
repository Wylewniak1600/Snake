from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(-40, 350)
        self.write(f'Score: {self.score}', font=('Arial', 16))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', font=('Arial', 16))

    def game_over(self):
        self.penup()
        self.goto(-85, 0)
        self.write('GAME OVER', font=('Arial', 25))
        self.hideturtle()

