"""
Etch-a-Sketch project
Create a turtle that goes forwards with 'w' key, backwards with 's', counterclockwise with 'a', and
clockwise with 'd'.
When 'c' is pressed, the drawing is cleared.

Use the turtle docs
"""
from turtle import Turtle, Screen


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def clear():
    # tim.clear just deletes the turtles drawings
    # different from screen.clear which deletes everything including the turtle
    tim.clear()
    tim.penup()
    tim.home()  # returns turtle to the origin, must raise pen before doing so or it will draw when resetting
    tim.pendown()


tim = Turtle()
tim.speed("fast")

screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()