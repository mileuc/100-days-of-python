#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random_letters = ""
random_symbols = ""
random_numbers = ""

#pick random letters
for number in range(0, nr_letters):
  random_index = random.randint(0, len(letters) - 1)
  random_letters += letters[random_index]

#pick random symbols
for number in range(0, nr_symbols):
  random_index = random.randint(0, len(symbols) - 1)
  random_symbols += symbols[random_index]

#pick random numbers
for number in range(0, nr_numbers):
  random_index = random.randint(0, len(numbers) - 1)
  random_numbers += numbers[random_index]

easy_password = random_letters + random_symbols + random_numbers
print(easy_password)

#hard solution
total_num_of_chars = nr_letters + nr_symbols + nr_numbers
hard_password = ""

#put the characters of the easy password into a list
list_of_password_chars = []
for character in easy_password:
  list_of_password_chars.append(character)

for character in range(0, total_num_of_chars):
  random_index = random.randint(0, len(list_of_password_chars) - 1)
  #choose random character from the easy password, remove it from the easy_password and add it to the hard password
  random_password_char = random.choice(list_of_password_chars)
  hard_password += random_password_char
  list_of_password_chars.remove(random_password_char)
  
print(hard_password)
