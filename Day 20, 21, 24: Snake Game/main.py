# main.py controls the snake game
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)  # 0 turns off the tracer, effectively saying 0 regular screen updates are done

snake = Snake()  # create instance of Snake class
food = Food()   # create instance of Food class
scoreboard = Scoreboard()  # create instance of Scoreboard class

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    # when tracer is turned off, tell program when to update and redraw the screen
    screen.update()  # call update after segments have moved, segments now appear at once (not piece-by-piece)
    time.sleep(0.075)  # adds a 0.1-second delay before code continues, after all three segments have moved

    snake.move()  # move the snake

    # step 4: detect collision with food, then create a new piece of food on screen in a random location
    if snake.head.distance(food) < 15:
        # compares the distance from the snake head to the specified coordinates
        # a turtle instance (like food) can also be passed as x, in which case y is not used
        # takes into account food is 10 by 10 and not the default 20 by 20, use 15 as a buffer
        food.relocate()
        snake.extend_snake()
        scoreboard.increase_score()

    # step 6: game-ending situation - detect collision with wall, show game over and stop snake movement
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        scoreboard.reset_scoreboard()
        snake.reset_snake()

    # step 7: game-ending situation - detect collision with any segment in the tail
    for segment in snake.segments[1:]:
        # bypass comparing distance from the snake head to the snake head (1st segment)
        # if segment == snake.head:
        #     pass
        # elif snake.head.distance(segment) < 5:
        #     game_is_on = False
        #     scoreboard.game_over()
        """Easier way to bypass first segment after using slicing"""
        if snake.head.distance(segment) < 5:
            scoreboard.reset_scoreboard()
            snake.reset_snake()

screen.exitonclick()