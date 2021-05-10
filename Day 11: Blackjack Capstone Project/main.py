############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

from random import choice
from art import logo
from replit import clear

print(logo)

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = choice(cards)
  return card

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(cards_list):
  """Take a list of cards and return the score calculated from the cards"""
  score = sum(cards_list)

  #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  if score == 21 and len(cards_list) == 2:
    return 0
  
  #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
  if 11 in cards_list and score > 21:
    cards_list.remove(11)
    cards_list.append(1)
    score = sum(cards_list)

  return score

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Both you and the computer have the same score.\nIt's a draw!"
  elif user_score == 0:
    return "Wow! You got blackjack! You win!" 
  elif computer_score == 0:
    return "Aww! The computer got blackjack! You lose!"
  elif user_score > 21:
    return "Aww! You went over. You lose!"
  elif computer_score > 21:
    return "The computer went over. You win!"
  else:
    if user_score > computer_score:
     return f"You have a score of {user_score}.\nThe computer has a score of {computer_score}. You win!"
    else:
      return f"You have a score of {user_score}.\nThe computer has a score of {computer_score}. You lose!"

def play_game():
  game_on = True

  user_cards = []
  computer_cards = []

  #Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
  #user_cards = []
  #computer_cards = []
  for i in range(0, 2):
    #NOTE: Use append not += when adding single items to a list. += is the same as extend, it must be adding a list.
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
  while game_on:
    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"  Your cards: {user_cards}, current score: {user_score}")
    print(f"  Value of computer's first card: {computer_cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_on = False
    else:
      #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
      valid_response = False
      while not valid_response:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if another_card == 'y':
          user_cards.append(deal_card())
          valid_response = True
        elif another_card == 'n':
          game_on = False
          valid_response = True
        else:
          print("Invalid response. Please try again.")
  
  #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f"\nYour final hand is {user_cards}")
  print(f"The computer has a hand of {computer_cards}")
  print(compare(user_score, computer_score))


#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
stop_game = False

while not stop_game:
  another_game = input("\nDo you want to play a game of Blackjack?\nType 'y' for yes or 'n' for no: ").lower()

  if another_game == 'n':
    clear()
    game_on = False
    print("Game over!")
    stop_game = True
  elif another_game == 'y':
    clear()
    print("Let's play!")
    play_game()
  else:
    print("Invalid response. Please try again!\n")
