# step 5: create a scoreboard and update the score when food is eaten
# scoreboard will be a turtle
from turtle import Turtle
ALIGNMENT = "center"
SCORE_FONT = ("Courier", 10, "normal")
GAME_OVER_FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # step 9: read and write to a file to save the high score and retrieve it
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()  # pen up before writing score and moving the turtle
        self.goto(x=0, y=275)
        self.create_scoreboard()

    def create_scoreboard(self):
        # adds text over the turtle
        self.write(arg=f"Score:  {self.score}  High Score: {self.high_score}",
                   move=False, align=ALIGNMENT, font=SCORE_FONT)

    # step 8: replace game_over with reset_scoreboard and reset_snake
    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0  # reset score
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write(arg=f"game over", move=False, align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()  # remove the previous score text before writing again
        self.write(arg=f"Score:  {self.score}  High Score: {self.high_score}",
                   move=False, align=ALIGNMENT, font=SCORE_FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
