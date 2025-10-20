from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.colors = self.load_colors()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.random_color = random.choice(self.colors)
        self.color(self.random_color)
        self.goto(random.randrange(-500, 500), random.randrange(-300, 300).__float__())

    def load_colors(self):
        try:
            with open('colors.txt', 'r') as file:
               return file.read().splitlines()
        except Exception as e:
            print(f"Error loading colors: {e}")


    def refresh(self):
        self.goto(random.randrange(-600, 600), random.randrange(-400, 400).__float__())
        self.random_color = random.choice(self.colors)
        self.color(self.random_color)