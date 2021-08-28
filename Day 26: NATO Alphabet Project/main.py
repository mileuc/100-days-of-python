"""
Review:
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
"""
"""
Take the CSV of the NATO Phonetic Alphabet, then follow the two TODO instructions.
Loop through the DataFrame, then create a new dictionary using a new key and new value.
"""
import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato_alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter: row.code for (index, row) in nato_alphabet_data.iterrows()}
print(data_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# while True:
    # valid_input = False
    # while not valid_input:
    #     user_input = input("Please enter a word: ").upper()
    #     # print(type(user_input))
    #
    #     if user_input.isalpha() and len(user_input) > 0:
    #         valid_input = True
    #     else:
    #         print("Please enter a valid string. Try again!")

    # word_list = [data_dict[letter] for letter in user_input]
    # print(word_list)


# TODO 3. Exception Handling - Alternative way
def generate_phonetic():
    user_input = input("Please enter a word: ").upper()
    if len(user_input) > 0:
        try:  # statement that might fail
            word_list = [data_dict[letter] for letter in user_input]
        except KeyError:  # if it fails because of a key error
            print("Sorry, only letters in the alphabet please!")
        else:  # if successful
            print(word_list)
        finally:    # regardless of success or fail
            generate_phonetic()  # give the user a chance to enter an input again
    else:
        print("You didn't enter anything! Try again!")
        generate_phonetic()


generate_phonetic()