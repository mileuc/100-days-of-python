# TODO: 3. quiz functionality - present each question to the user and ask them to answer it
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0    # keeps track of which question the user is currently on
        self.question_list = q_list  # list of Question objects
        self.score = 0

    # TODO: 3a. ask the questions
    def next_question(self):
        current_question = self.question_list[self.question_number]  # current Question object
        q_text = current_question.text  # access the text and answer attributes from each Question object
        q_answer = current_question.answer
        self.question_number += 1  # increase the question number once the text and answer have been extracted

        valid_answer = False
        while not valid_answer:
            user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ").capitalize()
            if user_answer == "True" or user_answer == "False":
                valid_answer = True
            else:
                print("Invalid answer.")

        self.check_answer(user_answer, q_answer)

    # TODO: 3b. check if the answer was correct
    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print("That's correct!")
            print(f"The correct answer was: {correct_answer}.")
        else:
            print("Incorrect.")
        print(f"Your current score is {self.score}/{self.question_number}.\n")

    # TODO: 3c. check if we're at the end of the quiz
    def still_has_questions(self):
        # simplified way to run the below if/else statement
        # return self.question_number < len(self.question_list)
        if self.question_number < len(self.question_list):
            return True
        else:
            return False



