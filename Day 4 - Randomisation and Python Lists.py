# Heads or Tails
import random

Toss = random.randint(0, 1)
if Toss == 1:
    print("And it is Heads")
else:
    print("So Tails it is")


# Who is going to pay
import random
names = random.randint(1, 5)

if names == 1:
    print("SRK")
elif names == 2:
    print("Salman")
elif names == 3:
    print("Aamir")
elif names == 4:
    print("Ranbir")
else:
    print("Amitabh")


# Nested list

Fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
Vegetabels = ["Spinach", "Kale", "Tomatoes", "Celery", "Patatoes"]

dirty_dozen = [Fruits, Vegetabels]

print(dirty_dozen)

list = 12345
list_str = str(list)
words = list_str.split("2")


# Project -- Rock - Papers - Scissors
# RULES 
# 1) Rock wins against Scissors
# 2) Scissors wins against Paper
# 3) Paper wins against Rock

import random
player = int(input("Welcome to Rock Paper and Scissors. Type 0 for Rock, 1 for Paper and 2 for Scissor\n"))
algorithm = random.randint(0, 2)
print(f"algorithm chose {algorithm}")
rock = 0
paper = 1
scissors = 2

if player >=3 or player <0:
    print("You have typed an invalid number, You lost")
elif algorithm == 0 and player == 2:
    print("Rock wins against Scissors, You lost")
elif algorithm == 1 and player == 0:
    print("Paper wins against Rock, You lost")
elif algorithm == 2 and player == 1:
    print("Scissors wins against Paper, You lost")
elif algorithm == 0 and player == 1:
    print("Paper wins against Rock, algorithm lost")
elif algorithm == 1 and player == 2:
    print("Scissors wins against Paper, algorithm lost")
elif algorithm == 2 and player == 0:
    print("Rock wins against Scissors, algorithm lost")
elif algorithm == player:
    print("It is a draw")




