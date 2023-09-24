# Day 2 - Data types

# 1. String
print("Hello"[3])

# 2. Integers
print("The addition of 12 & 34 is:")
print(12 + 34)

# Converting number into string
num_char = len(input("What is your name?\n"))
new_char = str(num_char)
print("Your name has" + " " + new_char + " " + "characters" )

# Exercise - Write a program that adds the digits in a 2 digit number e.g. if the input was
# 67, then the output should be 6 + 7 = 13.

two_digit_num = input("Type a two digit number: \n")
print(type(two_digit_num))
fd = two_digit_num[0]
sd = two_digit_num[1]
result = int(fd) + int(sd)
print("The addition of two digit no is:",result)

print(3 * 3 / 3 + 3 - 3)

# BMI Calculator - Write a program that calculates the Body Mass Index (BMI) from user's weight and height
# The BMI is calculated by dividing a persons's weight(kg) by the square of their height(m)
weight = input("What is your weight in kg\n")
height = input("What is your height in meter\n")

weight = int(weight)
height = float(height)
BMI = ((weight) / (height**2))
BMI = int(BMI)
print("Your BMI is :",(BMI))


# Create a program using maths and f-String and tell us how many days, weeks and months we left if we live until 
# 90 years old. It will take input as your current age and output a message with out time left in this format like
# You have x days, y months and z years left.
age = input("What is your age?:")
age = int(age)
years_remaining = 90 - age
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"You have {years_remaining}years, {months_remaining}months, and {days_remaining}days remaining")