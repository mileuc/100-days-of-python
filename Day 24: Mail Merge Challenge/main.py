# TODO: Create a letter using starting_letter.txt
with open("./Input/Names/invited_names.txt", mode="r") as names_data:
    names = names_data.readlines()  # return all lines in the file, as a list where each line is an item

with open("./Input/Letters/starting_letter.txt", mode="r") as letter_data:
    letter_template = letter_data.read()
    # print(letter_template)
    # for each name in invited_names.txt
    for name in names:
        stripped_name = name.strip()   # remove spaces at the beginning or end of the string
        # Replace the [name] placeholder with the actual name.
        named_letter = letter_template.replace("[name]", stripped_name)  # replace word in the string with another
        # Save the letters in the folder "ReadyToSend".
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as new_letter:
            new_letter.write(named_letter)

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
