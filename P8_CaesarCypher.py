# Caesar Cypher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',  'a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))

    shift %= 26
    caesar(text, shift, direction)

result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
if result == "no":
    should_continue = False
    print("Goodbye")


#for letter in text:
#     position = alphabet.index(letter)
#     if direction == "encode":
#         new_position = position + shift
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#         print(f"The encoded text is {cipher_text}")
#     elif direction == "decode":
#         new_position = position - shift
#         new_letter = alphabet[new_position]
#         plain_text += new_letter
#         print(f"The decoded text is {plain_text}")

# caesar(text,shift,direction)
# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position + shift
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")
#
#
#
# def decrypt(cipher_text, shift_amount):
#     decrypted_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift
#         decrypted_text += alphabet[new_position]
#     print(f"The decoded text is {decrypted_text}")
#
#
# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text,shift)

