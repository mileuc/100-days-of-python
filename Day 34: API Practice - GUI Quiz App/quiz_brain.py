import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        # correcting HTML entities that replace certain characters in HTML so it doesn't get confused with HTML code
        # step 2: use html.unescape to unescape the HTML results we get back from the API
        # eg. "A slug&rsquo;s blood is green." gets changed to "A slug’s blood is green."
        q_unescaped_text = html.unescape(self.current_question.text) # accessing text attribute in Question class

        # don't need this
        # user_answer = input(f"Q.{self.question_number}: {q_unescaped_text} (True/False): ")
        # self.check_answer(user_answer)

        return f"Q.{self.question_number}: {q_unescaped_text} "

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            # print("You got it right!")
            return True
        else:
            # print("That's wrong.")
            return False

        # print(f"Your current score is: {self.score}/{self.question_number}")
        # print("\n")
