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
