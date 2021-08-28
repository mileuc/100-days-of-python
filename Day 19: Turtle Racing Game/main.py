from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)  # fix the screen dimensions in pixels, use keyword args for clarity

race_is_on = False
# program starts with a pop-up that asks the user to bet on which coloured turtle will win the race
user_bet = screen.textinput(
    title="It's time to make a bet!",
    prompt="Which turtle will win the race? Enter a colour: "
)  # pop up a window for text input
# print(user_bet)

colors = ["red", "yellow", "green", "blue", "purple", "orange"]
all_turtles = []

# turtles line up in the starting position (left edge of screen) and make random steps to the right edge

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")  # shorthand method of setting the shape during initialization
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()  # avoids a line being drawn when goto is used
    # height is 400, y-axis spans from -200 to 200. first turtle starts at y=75 followed by gaps of 30
    new_turtle.goto(x=(-235), y=(75 - (turtle_index * 30)))  # since width is 500, x-axis from -250 to 250
    all_turtles.append(new_turtle)

# create a random number and tell the turtle to go forward by that amount, then repeat
# if a user bet is entered, start the race
if user_bet:
    race_is_on = True
# wait until user bet is entered before starting the race
while race_is_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        # apply winning condition, have to consider that a turtle is a 40 by 40 object
        if turtle.xcor() > 230:
            race_is_on = False
            winning_color = turtle.pencolor()  # color is a tuple that contains pencolor and fillcolor
            if winning_color.lower() == user_bet.lower():
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"Sorry, you lost. The {winning_color} turtle is the winner!")


# when the winning turtle reaches the finish line, print the name of the winning turtle and if you won/lost

screen.exitonclick()