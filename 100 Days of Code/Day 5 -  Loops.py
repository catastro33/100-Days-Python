Fruits = ['Apple', 'Banana', 'Mangoe', 'Peaches', 'Watermeleon']

for i in Fruits:
    print(i)

# 5.1 - Average Height
# You are going to write a program that calculate the average student height from the list of height.
# Average height should be rounded to a whole number.
# Importanat - You should not use sum() or len() function in your answer. You should try to replicate their functionality \n
# using what you have learnt about for loops.

student_heights = input("Input any 5 student's height\n").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
for height in student_heights:
    total_height += height
print("The total height of the students is:", total_height)

num_of_students = 0
for number in student_heights:
    num_of_students += 1
print("The total number of students is:", num_of_students)

avg_height = round(total_height / num_of_students)
print("The average height of the student is:", avg_height)

# -----------------------------------------------------------------------------------------
# Exercise 5.2 - Highest Marks

student_scores = input("Input a list of student score\n").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print("student_scores")

highest_score = 0
for score in student_scores:
    if score > highest_score:
     highest_score = score
print(f"The highest score is {highest_score}")
        

# ----------------------------------------------------------------------------------
# Exercise 5.3 - Adding Evens
# You are going to write a program that calculates the sum of all the even numbers from 1 to 100, including 1 and 100.
# IMPORTANT - There should only be one print statement in your console output. It should print the final total and not every step of the calculation.

Even_number = 0
for number in range(1,101):
    if number %2 == 0:
        Even_number += number
print(Even_number)


# --------------------------------------------------------------------------------------------
# Exercise 5.4 - Fizz Buzz
# You are going to write a program that automatically prints a solution to a Fizz Buzz game.
# INSTRUCTION:
# 1) Your program should print each number from 1 to 100 in turn.
# 2) When the number is divisible by 3 then instead of writing the number it should print "Fizz"
# 3) When the number is divisible by 5 then instead of writing the number it should print "Buzz"
# 4) And if the number is divisible by both 3 and 5 e.g 15 then instead of the number it should print "FizzBuzz"

for div_num in range(1, 101):
    if (div_num %3 == 0) and (div_num %5 == 0):
        print("Fizz Buzz")
    elif div_num %3 == 0:
        print("Fizz")
    elif (div_num %5 == 0):
        print("Buzz")
    else:
        print(div_num)


#----------------------------------------------------------------------------------------
# Exercise 5.5 - Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Password generator
Password = ""
for i in range(1, nr_letters + 1):
    Password += random.choice(letters)
    
for i in range(1, nr_symbols + 1):
    Password += random.choice(symbols)

for i in range(1, nr_numbers + 1):
    Password += random.choice(numbers)

print(f"Your Password is: {Password}")


# Hard Password generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


Password_list = []
for i in range(1, nr_letters + 1):
    Password_list.append(random.choice(letters))
    
for i in range(1, nr_symbols + 1):
    Password_list += random.choice(symbols)

for i in range(1, nr_numbers + 1):
    Password_list +=random.choice(numbers)

print(f"Your Password is: {Password_list}")
random.shuffle(Password_list)
print(Password_list)

New_pass = ""
for char in Password_list:
    New_pass += char

print(f"Your Password is {New_pass}")


# Multiplication Table
N = 5
for i in range(1, 10):
    result = N * i
    print(result, end=" ")


# You are given a string str, you need to print its characters at even indices(index starts at 0).
# Input: str = DoctorPhenomenal
# Output: DcoPeoea

# if you want user input then use first line
# input_word = input("Input your word\n")
strg = "DoctorPhenomenon"
word = ""
for i in range(0, len(strg), 2):
    word += strg[i]
print(word)

