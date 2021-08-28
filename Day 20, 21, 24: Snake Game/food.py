from turtle import Turtle
import random


class Food(Turtle):  # inherit from Turtle class, so the Food class will have the same capabilities
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)  # half of the original 20 by 20 size
        self.color("green")
        self.penup()
        self.speed("fastest")  # reduces animation size of food moving to location
        self.relocate()

    def relocate(self):
        random_x = random.randint(-280, 280)  # don't want it right at the edge, not -300 to 300
        random_y = random.randint(-280, 270)
        self.goto(x=random_x, y=random_y)






