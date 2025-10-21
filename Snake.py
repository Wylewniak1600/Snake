from turtle import Turtle


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.heading = 0

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        turtle = Turtle('square')
        turtle.color('white')
        turtle.penup()
        turtle.goto(position)
        self.segments.append(turtle)

    def tail_colision(self):
        collision = False
        for segment in self.segments[1:]:
            if segment.distance(self.head) < 10:
                collision = True
        return collision

    def make_longer(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(new_x, new_y)
        self.head.forward(20)

    def reset(self):
        for segment in self.segments:
            segment.goto(4000, 4000)

        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
            self.heading = 90

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
            self.heading = 270

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
            self.heading = 0

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
            self.heading = 180


