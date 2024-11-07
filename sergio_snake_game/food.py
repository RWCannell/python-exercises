import random
from snake import *


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.shape("turtle")
        self.speed("fastest")
        self.appear()
    def appear(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

