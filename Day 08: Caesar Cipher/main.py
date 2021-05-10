from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(cipher_direction, input_text, shift_amount):
  end_text = ""

  if cipher_direction.lower() == "encode":
    for char in input_text:
      if char in alphabet:
        alphabet_index = alphabet.index(char)
        if (alphabet_index + shift_amount) >= len(alphabet):
          #subtract the index by the length of the alphabet
          end_text += alphabet[alphabet_index + shift_amount - len(alphabet)]
        else:
          end_text += alphabet[alphabet_index + shift_amount]

      else:
        end_text += char

    print(f"The encoded text is {end_text}")

  elif cipher_direction.lower() == "decode":
    for char in input_text:
      if char in alphabet:
        alphabet_index = alphabet.index(char)
        if (alphabet_index - shift_amount) < 0:
          end_text += alphabet[alphabet_index - shift_amount + len(alphabet)]
        else:
          end_text += alphabet[alphabet_index - shift_amount]
      else:
        end_text += char

    print(f"The decoded text is {end_text}")

  else:
    print("Sorry, you didn't type 'encode' or 'decode'.\nPlease try again")

should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  shift = shift % len(alphabet)

  caesar(cipher_direction = direction, input_text = text, shift_amount = shift)

  continuing = input("Type 'yes' if you wish to continue. Otherwise, type 'no'.\n").lower()

  if continuing == 'no':
    should_continue = False
    print("Goodbye!")
