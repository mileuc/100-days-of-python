MORSE_CODE_CHART = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....",
    "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",
    "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
    "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----", ".": ".-.-.-",
    ",": "--..--", "'": ".----.", "?": "..--..", "!": "-.-.--", "/": "-..-.", "(": "-..--",
    ")": "-.--.-", "&": ".-...", ":": "---...", ";": "-.-.-.", "=": "-...-", "+": ".-.-.",
    "-": "-....-", "_": "..--.-", "$": "...-..-", "@": ".--.-."
}
CONTINUE_PROGRAM = True


def encrypt(text):
    encrypted_message = ""
    for letter in text:
        # extract each character (if not a space) one at a time and match it with its corresponding morse code
        if letter != " " and letter in MORSE_CODE_CHART:
            try:
                # add 1 space for different characters
                encrypted_message += (MORSE_CODE_CHART[letter] + " ")
            except KeyError:
                pass
        else:
            encrypted_message += "  "
            # add 2 spaces for different words
    return encrypted_message


def decrypt(morse_code):
    # add extra space to morse_code so the last morse_code_chars can be decrypted
    morse_code += " "

    decrypted_message = ""
    current_morse_char_to_decrypt = ""

    try:
        for char in morse_code:
            if char != " ":
                num_of_spaces = 0   # space counter
                current_morse_char_to_decrypt += char
            else:
                # if there is a space
                num_of_spaces += 1
                if num_of_spaces == 2:
                    # two spaces in morse = space in plain text
                    decrypted_message += " "
                else:
                    # just one space = means a new character, add the previous one to the decrypted msg
                    for key, value in MORSE_CODE_CHART.items():
                        if value == current_morse_char_to_decrypt:
                            decrypted_message += key
                    current_morse_char_to_decrypt = ""
    except KeyError:
        pass


    return decrypted_message




def main():
    while CONTINUE_PROGRAM:
        valid_response = False
        while not valid_response:
            method = input("Type 'encode' to encrypt to Morse code, or 'decode' to decrypt Morse code: ").lower()
            if method == "encode" or method == "decode":
                valid_response = True
            else:
                print("Sorry, you did not type 'encode' or 'decode'.\nPlease try again!")

        message = input("Enter your message: ").upper()
        print(f"You entered: {message}")

        if method == "encode":
            result = encrypt(message)
            print(result)
        else:
            result = decrypt(message)
            print(result)


if __name__ == "__main__":
    main()


