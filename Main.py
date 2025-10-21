import time
from Snake import Snake
from turtle import Turtle, Screen
from Food import Food
from Scoreboard import Scoreboard


class SnakeGame:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=1200, height=800)
        self.screen.bgcolor('black')
        self.screen.tracer(0)
        self.screen.listen()
        self.snake = Snake()
        self.x_wall = 600.0
        self.y_wall = 400.0
        self.snake_x_position = self.snake.head.xcor()
        self.snake_y_position = self.snake.head.ycor()
        self.food = Food()
        self.scoreboard = Scoreboard()
        self.game_is_on = True

    def eat_food(self):
        if self.snake.head.distance(self.food) < 20:
            self.food.refresh()
            self.scoreboard.update_scoreboard()
            self.snake.make_longer()

    def game_loop(self):
        while self.game_is_on:

            self.screen.update()
            time.sleep(0.1)

            self.snake.move()
            self.screen.onkey(self.snake.up, 'Up')
            self.screen.onkey(self.snake.down, 'Down')
            self.screen.onkey(self.snake.left, 'Left')
            self.screen.onkey(self.snake.right, 'Right')
            self.snake_x_position = self.snake.head.xcor()
            self.snake_y_position = self.snake.head.ycor()
            self.eat_food()

            if game.snake_x_position == game.x_wall or game.snake_y_position == game.y_wall or game.snake_x_position == -game.x_wall or game.snake_y_position == -game.y_wall:
                self.scoreboard.game_over()
                self.snake.reset()

            if game.snake.tail_colision():
                self.scoreboard.game_over()
                self.snake.reset()

        self.screen.exitonclick()


if __name__ == '__main__':
    game = SnakeGame()
    print(game.snake.head.heading)
    game.game_loop()