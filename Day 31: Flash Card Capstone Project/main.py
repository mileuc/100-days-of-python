from tkinter import *
import pandas
import random
# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
flip_timer = None
current_card = {}
# ---------------------------- CREATE NEW FLASH CARDS ------------------------------- #
try:
    cards_to_learn = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    cards_to_learn = pandas.read_csv("data/french_words.csv")
finally:
    # orient to have a list of dicts where keys=column names
    cards_to_learn_dict = cards_to_learn.to_dict(orient="records")
    print(cards_to_learn_dict)


def new_flash_card():
    global flip_timer, current_card

    current_card = random.choice(cards_to_learn_dict)
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")

    # After delay of 3s(3000ms), the card should flip and display the English translation for the current word.
    flip_timer = window.after(3000, flip_flash_card, current_card)


# ---------------------------- FLIP FLASH CARD ------------------------------- #


def flip_flash_card(card):
    canvas.itemconfig(card_background, image=card_back_img)
    # To change the text color in a canvas element, use the fill parameter
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=card["English"], fill="white")

    # get the delay countdown to stop after a new card is shown, next after() call will restart it from 0
    window.after_cancel(flip_timer)  # cancels the timer previously set up with after()


# ---------------------------- UPDATE PROGRESS ------------------------------- #
# when checkmark button is clicked, the user knows that word and it should be removed from the list of words to learn


def discard_card():
    window.after_cancel(flip_timer)  # cancels the timer previously set up with after()

    cards_to_learn_dict.remove(current_card)
    data = pandas.DataFrame(cards_to_learn_dict)  # new dataframe with updated data
    data.to_csv("./data/words_to_learn.csv", index=False)  # don't want indices for new csv on top of the existing ones

    new_flash_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Cards")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")  # cannot be called inside a function due to limited scope
card_background = canvas.create_image(400, 263, image=card_front_img)  # create image in canvas, center at this position
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))  # relative to canvas
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# buttons
unknown_button_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_button_img, command=new_flash_card, bg=BACKGROUND_COLOR, bd=0, relief=GROOVE)
unknown_button.grid(column=0, row=1)

known_button_img = PhotoImage(file="images/right.png")
known_button = Button(image=known_button_img, command=discard_card, bg=BACKGROUND_COLOR, bd=0, relief=GROOVE)
known_button.grid(column=1, row=1)

new_flash_card()  # generate a new flash card when the program starts, after UI is created

window.mainloop()