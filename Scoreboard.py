from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.load_high_score()
        self.color('white')
        self.penup()
        self.goto(-40, 350)
        self.write(f'Score: {self.score} High Score: {self.high_score}', font=('Arial', 16))
        self.hideturtle()

    def load_high_score(self):
        with open('high_score.txt', 'r') as f:
            self.high_score = int(f.read())
            return self.high_score

    def save_high_score(self):
        with open('high_score.txt', 'w') as f:
            f.write(str(self.high_score))

    def update_scoreboard(self):
        self.score += 1
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.write(f'Score: {self.score} High Score: {self.high_score}', font=('Arial', 16))

    def game_over(self):
        self.clear()
        self.score = 0
        self.write(f'Score: {self.score} High Score: {self.high_score}', font=('Arial', 16))


