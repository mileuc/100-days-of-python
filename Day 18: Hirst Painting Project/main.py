# Hirst Painting Project

# use colorgram package, which allows you to extract color from images
"""
to install package: file -> settings -> name of project -> project interpreter -> plus icon -> search for
colorgram.py -> install package -> close window and click OK
"""

"""
import colorgram

colors = colorgram.extract("hirst_painting.jpg", 25)  # extract a specified number of colors from the image
# print(colors)  # the extracted colors will either be RGB (what we want) or HSL

rgb_colors = []
for color in colors:
    # rgb_colors.append(color.rgb) # still won't have the format we need to use it inside turtle
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)  # manually remove the colors close to 255 (shades of white)
comment out the above code after forming the color list below

color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (186, 158, 53), (6, 57, 83),
              (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47),
              (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186),
              (172, 153, 159), (212, 183, 177), (176, 198, 203)]
"""
# use turtle to paint a 10 by 10 painting of spots that are 20 in size and spaced by 50 pixels apart
import turtle as turtle_module
import random


def turn_left():
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(50)


def turn_right():
    tim.right(90)
    tim.forward(50)
    tim.right(90)
    tim.forward(50)


def fill_row_left_direction():
    turn_left()
    for spot in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)


def fill_row_right_direction():
    turn_right()
    for spot in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)


tim = turtle_module.Turtle()
turtle_module.colormode(255)

color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (186, 158, 53), (6, 57, 83),
              (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47),
              (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186),
              (172, 153, 159), (212, 183, 177), (176, 198, 203)]

tim.hideturtle()
tim.penup()
tim.speed(0)

# move the initial turtle position closer to the bottom left corner
tim.setposition(-220, -210)

# initial bottom row
for initial_row_spot in range(10):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
# middle rows
for two_rows in range(4):
    fill_row_left_direction()
    fill_row_right_direction()
fill_row_left_direction()  # final row

screen = turtle_module.Screen()
screen.exitonclick()


