from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self, _distance):
        super().__init__()
        # Display Setup
        self.shape("circle")
        self.color("cyan")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")

        self.canvas_distance = _distance
        self.refresh()

    def refresh(self):
        # Position Calc
        random_x = random.randint(-self.canvas_distance, self.canvas_distance)
        random_y = random.randint(-self.canvas_distance, self.canvas_distance)
        self.goto(random_x, random_y)
