import turtle
import pandas


def get_mouse_click_coordinates(x, y):
    print(x, y)


screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=800, height=600)

# load in an image as a new shape
image = "blank_states_img.gif"  # turtle only works with the gif image format, hence why blank_states_img is a gif file
screen.addshape(image)  # now available to be used by turtle
us_map = turtle.Turtle()
us_map.shape(image)

# figure out the coordinates of each state relative to the game screen
"""
How? Google 'get x y coordinate on click python turtle'. Solution below.
Click coordinates for each state already recorded in the CSV file
"""

# turtle.onscreenclick(get_mouse_click_coordinates) # click will call function and pass coordinates of click location

# challenge: check the user answer against all the states in the CSV file
data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()

correct_answers = 0
states_found = []
# states_missed = []
number_of_states = data.state.count()

while correct_answers < 50:
    # ask user for an answer
    answer_state = screen.textinput(title=f"{correct_answers}/{number_of_states} States Correct",
                                    prompt="Enter the name of another state!").title()
    # capitalizes each word in the string, as opposed to capitalize() which only capitalizes the first word

    # exit code to break the while loop and end the game
    if answer_state == "Exit":
        # generate a CSV file with the states that were missed

        # old method
        # for state in states_list:
        #     if state not in states_found:
        #         states_missed.append(state)

        # with list comprehension
        states_missed = [state for state in states_list if state not in states_found]
        new_data = pandas.DataFrame(states_missed)  # 1-column dataframe
        new_data.to_csv("states_to_learn.csv")
        break

    # if answer matches a state in the CSV file, write the name of the state on the screen at the correct coordinates
    if answer_state in states_list and answer_state not in states_found:
        states_found.append(answer_state)
        state_label = turtle.Turtle()
        state_label.hideturtle()
        state_label.penup()

        correct_state_data = data[data.state == answer_state]  # pull out the row with the answer
        correct_answers += 1

        state_label.goto(x=int(correct_state_data.x), y=int(correct_state_data.y))
        state_label.write(f"{answer_state}", align="left", font=("Arial", 8, "normal"))

    # otherwise nothing happens and the input box appears again

# turtle.mainloop()  # alternative way of keeping the screen open when the code is finished running
screen.exitonclick()  # no longer needed with the use of turtle.mainloop
