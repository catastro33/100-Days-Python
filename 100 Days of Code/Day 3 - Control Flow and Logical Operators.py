# Day 3 - Control Flow and Logical Operators

# Write a code that will decide wheather you can ride a roller coaster.

print("Welcome to Essel World")

height = int(input("What is your height in CM:\n"))

if height >= 120:
    print("Yeahhh!! You can ride the Rolller Coaster")
else:
    print("Complain pee chote :) :)")


# ----------------------------------------------------------
# Exercise - Write a program that works out whether if a given number is odd or even number.
print("Welcome to Odd or Even check")
number = int(input("Input your number:\n"))

if number %2 == 0:
    print("This is even number")
else:
    print("This is an odd number")


#------------------------------------------------------------
# Nested if-else 
print("Welcome to Essel World")

height = int(input("What is your height in CM:\n"))

if height >= 120:
    print("Yeahhh!! You can ride the Rolller Coaster")
    age = int(input("What is your age?\n"))
    if age >= 15:
        print("Your amount will be $12, Have fun")
    else:
        print("Your total will be only $7, Enjoy your ride")
else:
    print("Complain pee chote :) :)")


#----------------------------------------------------------------
# elif statement
print("Welcome to Essel World")

height = int(input("What is your height in CM:\n"))

if height >= 120:
    print("Yeahhh!! You can ride the Rolller Coaster")
    age = int(input("What is your age?\n"))
    if age < 11:
        print("Sorry you can't ride")
    elif age <= 12:
        print("Your amount will be $5")
    elif age <=18:
        print("Your total will be only $7, Enjoy your ride")
    else:
        print("You have to pay $12")
else:
    print("Complain pee chote :) :)")

#-----------------------------------------------------------------------------
# BMI Calculator 2.0
# Write a program that interprets the Body Mass Index (BMI) based on user's weight and height.
# It should tell them the interpretation of their BMI based on the BMI value.
# Under 18.5 they are underweight.
# Over 18.5 but below 25 they have a normal weight.
# Over 30 but below 35 they obese.
# Above 35 they are clinically obese.

print("This is a BMI Calculator")

weight = (float(input("What is your weight in KG?\n")))
height = (float(input("What is your height in meter?\n")))

BMI = ((weight) / (height**2))
BMI = round(BMI)

if BMI <= 18.5:
    print(f"Your BMI is: {BMI}, You are underweight.")
elif BMI < 25:
    print(f"Your BMI is: {BMI}, You have a normal weight.")
elif BMI < 30:
    print(f"Your BMI is: {BMI}, You are overweight")
elif BMI < 35:
    print(f"Your BMI is: {BMI}, Your are obese")
else:
    print(f"Your BMI is: {BMI}, Your are clinically obese")


#-------------------------------------------------------------------------------
# Leap year calculator
# Instructions - Write a program that works out whether if a given year is a leap year
# This is how your work out whether if a particular year is leap year.
# On every year that is evenly divided by 4
# Except every year that is evenly divisible by 100
# Unless the year is also evenly divisible by 400

year = int(input("Please input your year of choice\n"))

if year %4 == 0:
    if year %100 == 0:
        if year %400 == 0:
            print("This is a leap year")
        else:
            print("This is not a leap year")
    else:
        print("This is a leap year")
else:
    print("This is not a leap year")


#--------------------------------------------------------
# Multiple if statements 
# We will use the roller coaster problem and this time we will ask customers, do they want photos
# using multiple if statements.

print("Welcome to Essel World")

height = int(input("What is your height in CM:\n"))
bill = 0

if height >= 120:
    print("Yeahhh!! You can ride the Rolller Coaster")
    age = int(input("What is your age?\n"))
    if age < 11:
        print("Sorry you can't ride")
    elif age <= 12:
        bill == 5
        print("Your amount will be $5")
    elif age <=18:
        bill == 7
        print("Your total will be only $7, Enjoy your ride")
    else:
        bill = 12
        print("You have to pay $12")
    
    photo = input("Do you want to get clicked?\n")
    if photo == "Yes":
        bill = bill + 3
        
    print(f"Your total is ${bill}")

else:
    print("Complain pee chote :) :)")


#------------------------------------------------------------
# Pizza Order
# Based on user's order, work out their final bill.
# Small Pizza - $15
# Medium Pizza - $20
# Large Pizza - $25
# Pepperoni for small pizza - +$2
# Pepperoni for medium or large pizza - +$3
# Extra cheeze for any size - $1

print("Welcome to Pizza Hut!!!")
size = input("Which pizza size do you want? s, m, l\n")
pepperoni = input("Do you want pepperoni? Y or N\n")
cheeze = input("Do you also want cheeze? Y or N\n")

bill = 0


if size == "s":
    bill += 15
elif size == "m":
    bill += 20
else:
    bill += 25
    

    
if pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3
        

if cheeze == "y":
    bill += 1

print(f"Your total is ${bill}")


#------------------------------------------------------
# Logical Operators - AND, OR, NOT

print("Welcome to Essel World")

height = int(input("What is your height in CM:\n"))
bill = 0

if height >= 120:
    print("Yeahhh!! You can ride the Rolller Coaster")
    age = int(input("What is your age?\n"))
    if age < 11:
        print("Sorry you can't ride")
    elif age <= 12:
        bill == 5
        print("Your amount will be $5")
    elif age <=18:
        bill == 7
        print("Your total will be only $7, Enjoy your ride")
    elif age >= 45 and age <= 55:
        print("Everything will be fine, the ride is on the house")
    else:
        bill = 12
        print("You have to pay $12")
    
    photo = input("Do you want to get clicked?\n")
    if photo == "Yes":
        bill = bill + 3
        
    print(f"Your total is ${bill}")

else:
    print("Complain pee chote :) :)")


#--------------------------------------------
# Love Calculator
# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:
# 1) Take both person's names and check for the number of times the letters in the word TRUE occurs.
# 2) Then check for the number of times the letters in the word LOVE occurs. 
# 3) Then combine these numbers to make a 2 digit number.

# For love score less than 10 or greater than 90, the message should be:
# "Your score is x, you go together like coke and mentos."

# For love score between 40 and 50, the message should be:
# "Your score is y, you are alright together."

# Otherwise, the message will just be their score. eg:
# "Your score is z."

print("Welcome to Love Calculator")
name_1 = input("What is your name?\n")
name_2 = input("What is their name?\n")

comb_str = name_1 + name_2
low_comb_str = comb_str.lower()

t = low_comb_str.count("t")
r = low_comb_str.count("r")
u = low_comb_str.count("u")
e = low_comb_str.count("e")
true = t + r + u + e

l = low_comb_str.count("l")
o = low_comb_str.count("o")
v = low_comb_str.count("v")
e = low_comb_str.count("e")
love = l + o + v + e

love_score = int(str(true) + str(love))

print(love_score)

if (love_score > 1) and (love_score < 50):
    print(f"Your love score is {love_score}, Meh") 
elif (love_score >= 50) and (love_score <= 70):
    print(f"Your love score is {love_score},work on it")
elif (love_score >= 70) and (love_score <= 80):
    print(f"Your love score is {love_score}, Doing fine")
else:
    print("Hello!!!! Love birds")


#------------------------------------------------------------
# Project - Treasure Island

print("Welcome to Treasure Island. Your mission is to find treasure")
choice1 = input('You are at a crossroad, where do you want to go? "left" or "right"\n')

if choice1 == "left":
    choice2 = input('Your have came across a lake, you have to go to an island. Do you want to "swim" or "wait" for the boat?\n').lower()
    if choice2 == "wait":
        choice3 = input('You have arrived on the island unharmed. You have to enter the house. You have 4 choices "red", "green", "white" or black\n').lower()
        if choice3 == "red":
            print("You have been eaten by the beast, Game Over")
        elif choice3 == "green":
            print("You have been poisened, Game Over")
        elif choice3 == "white":
            print("Congratulations, You have won the treasure!!!!")
        else:
            print("You have entered the door of doom, Game Over")
    else:
        print("You have no patience. You have been eaten by a Crocodile")
else:
    print("Ye kahan aa gae aap? Game Over")

