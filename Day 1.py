# Day 1
print("Hello world!")

# To print the two sentences on two different line 
print("What is up guys \nWhazz up ma dawggg")

# String concatination
print("Hello" + "How are you?")

print("Hello!! " + "\nHow are you?")

# Debugging
print("Day 1 - String Manipulation")
print('String conncatination is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New line can be created with a backslash and n.")

print('Hello ' + input("What is your name?") + '!')


# Write a program that write the number of characters in a user's name.
char_len=len(input("What is your name? "))
print(char_len)

# Or we can do this way
name = input('What is your name? ')
length = len(name)
print(length)

# Wrtie a program to switch a values stored in the variables 'a' and 'b'
a = input("a:")
b = input("b:")
c = a
a = b
b = c
print("a = " + a)
print("a = " + b)


## Project - Band Name Generator
# Make sure that the input cursor shows on a new line. 

# 1. Create a greeting for your program
Greetings = "Hello there muzzic loverss"
print(Greetings)

# 2. Ask the user for the city that they grew up in
city_name = input("What city do you live in? \n")

# 3. Ask the user for the name of their pet.
pet_name = input("What is the name of your pet? \n")

# 4. Combine the name of their city and pet and show them their band name.
band_name = city_name + " " + pet_name
print("Your band name is " + band_name)