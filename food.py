from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        self.goto(x, y)
        self.refresh()

    def refresh(self):
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        self.goto(x, y)


