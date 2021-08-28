# Step 3: Build a class-based Tkinter UI
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):  # quiz_brain passed in must be of type QuizBrain when QuizBrain is init
        self.quiz = quiz_brain

        self.window = Tk()  # make window a property of this class
        self.window.title("Quizzer")
        # can code up UI inside init just like we did for other UIs
        self.window.config(padx=20, bg=THEME_COLOR)

        # score label
        self.score_label = Label(text="Score: 0", font=("Arial", 12, "bold"), bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0, pady=20)

        # canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,  # slightly less than the canvas width, used to get text to wrap and be on separate lines
            text="Question",
            font=FONT,
            fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        # buttons
        true_img = PhotoImage(file="images/true.png")   # self not used because it's only used to set up the button
        self.true_button = Button(image=true_img, command=self.press_true, bg=THEME_COLOR, bd=0, relief=GROOVE)
        self.true_button.grid(column=0, row=2, pady=20)
        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, command=self.press_false, bg=THEME_COLOR, bd=0, relief=GROOVE)
        self.false_button.grid(column=1, row=2, pady=20)

        # call get_next_question() when program runs and UI is initialized
        self.get_next_question()

        self.window.mainloop()  # like a never-ending while loop, always checking for updates in GUI

    # Step 4: Populate UI with questions from API
    def get_next_question(self):
        self.canvas.config(bg="white")  # reset canvas
        # Step 7: Update score
        self.score_label.config(text=f"Score: {self.quiz.score}")
        # check if we can get the next question, in case we're on the last question
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            # disable true and false buttons at the end of the quiz
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    # Step 5: Go into quiz_brain and check the answer when a button is pressed
    def press_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def press_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    # Step 6: Give user feedback after user enters question
    def give_feedback(self, is_right):
        # change canvas colour to green or red, delay for 1 second, then revert to original colour
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        # time.sleep() won't work since we are using mainloop that runs continuously
        self.window.after(1000, self.get_next_question)
