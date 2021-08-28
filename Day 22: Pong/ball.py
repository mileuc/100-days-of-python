# step 3: create and move the ball
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(x=0, y=0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # when bounce occurs off top or bottom wall, y_move is changed so the ball moves in opposite way
        self.y_move *= -1

    def bounce_x_left_paddle(self):
        self.x_move = (abs(self.x_move))
        self.move_speed *= 0.9  # step 8: change ball speed every time ball hits paddle

    def bounce_x_right_paddle(self):
        self.x_move = -(abs(self.x_move))
        self.move_speed *= 0.9

    def left_paddle_miss(self):
        self.goto(x=0, y=0)
        self.move_speed = 0.05  # reset ball speed when it resets
        self.bounce_x_left_paddle()

    def right_paddle_miss(self):
        self.goto(x=0, y=0)
        self.move_speed = 0.05
        self.bounce_x_right_paddle()