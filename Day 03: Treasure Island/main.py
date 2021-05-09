print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

first_step = input("You wake up above somebody's lip and see two nostrils.\nLeft or right? ")
if (first_step.lower() == "left"):
  second_step = input("A sea of phlegm engulfs the vicinity.\nSwim or wait? ")
  if(second_step.lower() == "wait"):
    third_step = input("A boat(booger) arrives and you ride it to an area with three doors. Which door?\nRed, yellow, or blue? ")
    if(third_step.lower() == "yellow"):
      print("You successfully escaped and won. Congratulations!")
    elif(third_step.lower() == "red"):
      print("You got engulfed in flames. Game over. Hit the bricks, goofy.")
    elif(third_step.lower() == "blue"):
      print("You enter the blue door, only to get crushed by blue balls. Game over. Hit the bricks, goofy.")
    else:
      print("You didn't even pick one of the three options. Got turned into poop. Game over. Hit the bricks, goofy.")
  else:
    print("You got attacked and were eventually eaten by worms. Game over. Hit the bricks, goofy.")
else:
  print("You fell into a hole of never-ending darkness. Game over. Hit the bricks, goofy.")
