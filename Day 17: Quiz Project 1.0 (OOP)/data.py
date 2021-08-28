# question_data = [
#     {"text": "A slug's blood is green.", "answer": "True"},
#     {"text": "The loudest animal is the African Elephant.", "answer": "False"},
#     {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
#     {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
#     {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, "
#              "you are free to take it home to eat.", "answer": "True"},
#     {"text": "In London, UK, if you happen to die in the House of Parliament, "
#              "you are entitled to a state funeral.", "answer": "False"},
#     {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
#     {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
#     {"text": "Google was originally called 'Backrub'.", "answer": "True"},
#     {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
#     {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
#     {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
# ]

# generating more questions from Open Trivia DB at https://opentdb.com/api_config.php
# API generates data in JSON format. Paste the entire JSON in, then click Code -> Reformat Code
# has two key-value pairs: response _code and results
# results has 10 (or however many you created) dictionaries. You can delete {"response_code": 0, "results": [
# this will leave just the list of dictionaries, each with 5 key-value pairs
# the question and correct_answer keys are what we're interested in. modify these keys in main.py accordingly.
question_data = [
    {"category": "Entertainment: Television", "type": "boolean", "difficulty": "medium",
     "question": "The television show Doctor Who first aired in 1963.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Entertainment: Television", "type": "boolean", "difficulty": "medium",
     "question": "In the TV series Red Dwarf, Kryten's full name is Kryten 2X4B-523P.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Television", "type": "boolean", "difficulty": "medium",
     "question": "Like his character in 'Parks and Recreation', Aziz Ansari was born in South Carolina.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Television", "type": "boolean", "difficulty": "medium",
     "question": "Bob Ross was a US Air Force pilot.", "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Entertainment: Television", "type": "boolean", "difficulty": "medium",
     "question": "Klingons respect their disabled comrades, and those who are old, injured, and helpless.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Entertainment: Television", "type": "boolean", "difficulty": "medium",
     "question": "In 'Star Trek', Klingons respect William Shakespeare, they even suspect him having a Klingon lineage.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Television", "type": "boolean", "difficulty": "medium",
     "question": "Klingons once had a period of Democracy in their history, they referred to it as the 'Dark Times'.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Television", "type": "boolean", "difficulty": "medium",
     "question": "In 'Star Trek', Klingons are commonly referred to as 'Black Elves'.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Entertainment: Television", "type": "boolean", "difficulty": "medium",
     "question": "In 'Star Trek: The Next Generation', Data is the only android in existence.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Entertainment: Television", "type": "boolean", "difficulty": "medium",
     "question": "An episode of 'The Simpsons' is dedicated to Moe Szyslak's bar rag.",
     "correct_answer": "True", "incorrect_answers": ["False"]}
]
