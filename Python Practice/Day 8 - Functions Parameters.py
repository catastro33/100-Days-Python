# Functions and input

# Positional arguments
def greetings(name, location):
    print(f"Hello there {name}, how are you doing?")
    print(f"How is it to be in {location}?")

greetings("Sam", "London")

# Keyword arguments
def greetings(name, location):
    print(f"Hello there {name}, how are you doing?")
    print(f"How is it to be in {location}?")

greetings(location="London", name="Sam")

# Paint Area Calculator
def paint_cal(height, width, cover):
    print(f"You will need {round_off} cans of paint")

wall_height = int(input("Height of wall: "))
wall_width = int(input("Width of wall: "))
num_of_cans = ((wall_height * wall_width) / 5)
round_off = round(num_of_cans)
coverage = 5
paint_cal(height = wall_height, width = wall_width, cover = coverage)


# Prime Number Checker

def prime_checker(number):
    is_true = True
    for i in range(2, number):
        if number % i == 0:
            is_true = False
        
    if is_true:
        print("It is Prime Number")
    else:
        print("It is a Composite Number")

n = int(input("Check this number: \n"))
prime_checker(number = n)


# Ceaser Cipher Enrcyption
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'Encode' to Encrypt, type 'Decode' to Decrypt:\n")
Text = input("Input your message:\n").lower()
Shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_number):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_number
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

# encrypt(plain_text=Text, shift_number=Shift)

def decrypt(plain_text, shift_number):
    decipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position - shift_number
        new_letter = alphabet[new_position]
        decipher_text += new_letter
    print(f"The decoded text is {decipher_text}")

# decrypt(plain_text=Text, shift_number=Shift)

if direction == "Encode":
    encrypt(plain_text=Text, shift_number=Shift)
elif direction == "Decode":
    decrypt(plain_text=Text, shift_number=Shift)