from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# step 1: create screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  # turns off the animation and screen refresh

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))  # pass in the position of each paddle as a tuple
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(left_paddle.up, "a")
screen.onkeypress(left_paddle.down, "z")
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)  # get while loop to sleep for a bit between each update, in order to slow the ball down
    screen.update()  # refreshes screen
    ball.move()

    # step 4:  detect collision with either the top or bottom wall and make it bounce
    if ball.ycor() > 280 or ball.ycor() < -280:  # since ball is 20 by 20 pixels
        ball.bounce_y()   # bounce and change the y-coordinate (vertical) movement

    # step 5:  detect collision with paddle and make it bounce off the paddle
    """
    problem: the distance method would check the balls distance to the center of the paddle, not the edge
    
    solution: add an additional condition to account for this: if the ball has gone past a certain point on the x-axis,
    and is within a 50 pixel distance of the paddle, then this means it also made contact with the paddle
    """
    # detect collision with left paddle
    # reminder x-axis spans from -400 to 400
    if ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x_left_paddle()  # bounce and change the x-coordinate (horizontal) movement

    # detect collision with right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x_right_paddle()

    # step 6:  detect when ball goes out of bounds
    # should trigger a restart of the game where ball is back in the center and goes in the opposite direction
    # detect right paddle miss, taking into account the paddle spans from 340 to 360 since it's positioned at 350
    if ball.xcor() > 380:
        ball.right_paddle_miss()
        scoreboard.left_point()

    # detect left paddle miss
    if ball.xcor() < -380:
        ball.left_paddle_miss()
        scoreboard.right_point()

screen.exitonclick()


# step 8: change ball speed
