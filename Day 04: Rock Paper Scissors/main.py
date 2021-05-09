rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

game_images = [rock, paper, scissors]
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors \n"))
opponent_choice = random.randint(0, 2)

if 0 <= your_choice <= 2:
  print(game_images[your_choice])
else:
  print(f"Your choice of {your_choice} is an invalid response.")

if 0 <= opponent_choice <= 2:
  print("Computer chose:")
  print(game_images[opponent_choice])

if (your_choice == 0):
  if (opponent_choice == 1):
    print("You lose")
  elif (opponent_choice == 2):
    print("You win")
  else:
    print("Draw")
elif (your_choice == 1):
  if (opponent_choice == 0):
    print("You win")
  elif(opponent_choice == 2):
    print("You lose")
  else:
    print("Draw")
elif (your_choice == 2):
  if(opponent_choice == 0):
    print("You lose")
  elif(opponent_choice == 1):
    print("You win")
  else:
    print("Draw")
else:
  print("You typed an invalid number. You lose!")
