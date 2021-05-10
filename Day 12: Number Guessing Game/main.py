from art import logo
from replit import clear
from random import choice

# Allow the user to choose a difficulty
def choose_difficulty():
  """Allows the user to pick a game difficulty of either 'easy' or 'hard'"""
  valid_difficulty = False
  while not valid_difficulty:
    difficulty = input("Please choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy" or difficulty == "hard":
      valid_difficulty = True
    else:
      print("Invalid Response.")

  return difficulty

# Generate and return a random number between 1-100
def random_number():
  """Generates and returns a random number between 1 and 100."""
  return choice(range(1, 101))
  
def play_game(mode, number):
  """Activate the Number Guessing Game"""
  game_on = True
  if mode == "hard":
    lives = 5
  else:
    lives = 10

  while game_on:
    print(f"You have {lives} attempts remaining to guess the number.")
    valid_guess = False
    while not valid_guess:
      guess = int(input("Make a guess: "))
      if 1 <= guess <= 100:
        if guess == number:
          print("You guessed right! You win!")
          game_on = False
        elif guess > number:
          print("Too high!")
          lives -= 1
        elif guess < number:
          print("Too low!")
          lives -= 1
        valid_guess = True
      else:
        print("Invalid guess!")
    
    if lives == 0:
      print("You have 0 attempts remaining. Game over!")
      game_on = False
    
print(logo)
print("Welcome to the Number Guessing Game!")
difficulty = choose_difficulty()
play_game(difficulty, random_number())

game_over = False
# Ask the user if they wish to play again.
while not game_over:
  play_again = input("Do you want to play again?\nPress 'y' for yes or 'n' for no: ").lower()
  if play_again == 'y':
    clear()
    difficulty = choose_difficulty()
    play_game(difficulty, random_number())
  elif play_again == 'n':
    clear()
    print("Thanks for playing!")
    game_over = True
  else:
    print("Invalid response.")

