from turtle import Turtle
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()

    def refresh(self):
        self.color(random.choice(colors))
        position = random.randint(-320, 320), random.randint(-320, 320)
        self.goto(position)
