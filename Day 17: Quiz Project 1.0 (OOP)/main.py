from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from random import shuffle

# TODO: 2. creating a question bank of Question objects
# question_data is a list of dictionaries
question_bank = []  # this will be a list of Question objects
for question in question_data:  # for each dictionary in the list, access their text and answer with respective keys
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)  # forming a new Question object from each dictionary
    question_bank.append(new_question)

# shuffle orders of the questions before passing the list to the QuizBrain and starting the quiz
shuffle(question_bank)
quiz = QuizBrain(question_bank)

# if quiz still has questions remaining:
while quiz.still_has_questions():
    # if quiz.question_number < len(quiz.question_list):  # done to avoid error after the last question
    quiz.next_question()

print("Thanks for playing!")
print(f"Your final score is {quiz.score}/{quiz.question_number}.")
