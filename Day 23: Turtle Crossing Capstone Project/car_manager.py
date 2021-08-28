"""
Step 2:
Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the
left edge of the screen. No cars should be generated in the top and bottom 50px of the screen (think of
it as a safe zone for our little turtle).

Hint: generate a new car only every 6th time the game loop runs.
"""
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10  # amount the car move distance increases with each level


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        # 1 in 6 chance of creating a new car, to reduce the frequency of creation
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_cars = Turtle(shape="square")
            new_cars.shapesize(stretch_len=2, stretch_wid=1)  # by default, a turtle is 20 by 20
            new_cars.penup()
            new_cars.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_cars.goto(x=300, y=random_y)
            self.all_cars.append(new_cars)

    # move cars across the screen from right to left
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
