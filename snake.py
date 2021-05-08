from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        """Creates snake body with 3 segments"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(position)
        self.snake_body.append(new_segment)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def reset(self):
        for segment in self.snake_body:
            segment.goto(1200, 1200)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

    def move(self):
        """Makes snake move forward with the tail following its head"""
        for segment in range(len(self.snake_body) - 1, 0, -1):
            next_position = (self.snake_body[segment - 1].xcor(), self.snake_body[segment - 1].ycor())
            self.snake_body[segment].goto(next_position)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Turn snake up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Turn snake down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Turn snake left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Turn snake right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
