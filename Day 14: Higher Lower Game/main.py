from game_data import data 
from art import logo, vs
from replit import clear
from random import choice

# List of steps
# generate two items and put them in a list
# ensure the two items are different
# ensure the follower counts are different

# print information about the item name, description, location 

# take user input about which item they think has more followers

# compare the amount of followers between the two 

# check if the user's answer matches the follower count 

# if user gets it right:
# increase current score by 1
# the second item in the list becomes the first item
# first item gets moved to a list of used items, to ensure it's never
# used again
# repeat loop again with updated score shown
# if the user gets it wrong:
# end game/loop
# print game over and the final score


# generate two random items and put them in a list
def random_items():
  """Generate two random items and return them as a list."""
  items = []
  follower_count = 0
  for i in range(0, 2):
    items.append(choice(data))
    if items[i]['follower_count'] == follower_count:
      items.remove(items[i])
      items.append(choice(data))
    else:
      follower_count = items[i]['follower_count']

  return items

# make the second item the first item in the list and generate a new item in it's place.
def shift_items(items):
  """Make the second item the first item in the list and generate a new item in it's place."""
  # remove first item
  items.remove(items[0])
  # add new item and return the new sets 
  items.append(choice(data))

  follower_counts_different = False
  while not follower_counts_different:
    if items[0]['follower_count'] == items[1]['follower_count']:
      items.remove(items[1])
      items.append(choice(data))
    else:
      follower_counts_different = True

  return items

def compare_followers(first_item, second_item, guess):
  """Compare the amount of followers from each item to determine the correct answer."""
  if first_item['follower_count'] > second_item['follower_count']:
    return 'A'
  elif second_item['follower_count'] > first_item['follower_count']:
    return 'B'
  else:
    return "Neither"

def check_answer(guess, answer):
  """Compare the user's guess to the correct answer"""
  if guess == answer:
    return True
  else:
    return False

def play_game(first_item, second_item):
  """Print out the two items that the user must compare, take their guess, and check the guess against the correct answer to determine if the game continues and they get points."""
  print(f"Compare A: {first_item['name']}, a {first_item['description']}, from {first_item['country']}.")
  print(vs)
  print(f"Compare B: {second_item['name']}, a {second_item['description']}, from {second_item['country']}.")

  valid_guess = False
  while not valid_guess:
    user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    if user_guess == 'A' or user_guess == 'B':
      valid_guess = True
    else:
      print("Invalid response.")

  correct_answer = compare_followers(first_item, second_item, user_guess)

  is_correct = check_answer(user_guess, correct_answer)

  #print(is_correct)
  if is_correct == True:
    clear()
    return True
  else:
    clear()
    print(f"Sorry! That's wrong. Final score: {current_score}")
    return False

#initial turn
game_on = True
while game_on:
  current_score = 0
  items = random_items()
  item_1 = items[0]
  item_2 = items[1]
  print(logo)
  game_continues = play_game(item_1, item_2)
  current_score += 1

  items = shift_items(items)
  item_1 = items[0]
  item_2 = items[1]

  #subsequent turns, if initial turn was successful
  while game_continues:
    print(logo)
    print(f"You're right! Current score: {current_score}")
    game_continues = play_game(item_1, item_2)
    #loop will break if this returns false immediately
    current_score += 1

    items = shift_items(items)
    item_1 = items[0]
    item_2 = items[1]

  valid_input = False
  while not valid_input:
    play_again = input("Do you want to play again? Type 'y' for yes or 'n' for no: ").lower()
    if play_again == 'y':
      clear()
      valid_input = True
    elif play_again == 'n':
      clear()
      print("Thanks for playing!")
      valid_input = True
      game_on = False
    else:
      print("Invalid input.")
