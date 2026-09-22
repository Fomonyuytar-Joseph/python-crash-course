alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

direction = input("Type 'encode' to encrypt , type 'decode' to decrypt:\n")

text = input("Type your message:\n").lower()

shift = int(input("Type the shift number:\n"))

should_continue = True

while should_continue:

    def caesar(plain_text, shift_amount, cipher_direction):
        cipher_text = ""
        for letter in plain_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = 0
                if cipher_direction == "encode":
                    new_position = (position + shift_amount) % len(alphabet)
                elif cipher_direction == "decode":
                    new_position = (position - shift_amount) % len(alphabet)
                cipher_text += alphabet[new_position]

        print(f"The {cipher_direction}d text is {cipher_text}")

    caesar(text, shift, direction)
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == 'no':
        should_continue = False
        print("Good bye!")
    


# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         if letter in alphabet:
#             position = alphabet.index(letter)
#             new_position = (position + shift_amount) % len(alphabet)
#             cipher_text += alphabet[new_position]

#         else:
#             cipher_text += letter
#     print(f"The encoded text is {cipher_text}")


# def decrypt(encrypt_text, shift_amount):
#     decrypt_text = ""
#     for letter in encrypt_text:
#         if letter in alphabet:
#             position = alphabet.index(letter)
#             new_position = position - shift_amount
#             decrypt_text += alphabet[new_position]
#         else:
#             decrypt_text += letter
#     print(f"The decrypted text is {decrypt_text}")


# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)
