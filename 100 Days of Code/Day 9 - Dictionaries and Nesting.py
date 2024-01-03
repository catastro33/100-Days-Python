# Day 9 - Dictionaries and Nesting

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."}

# Retrieving an item from a dictionary
print(programming_dictionary["Bug"])

# Adding new item to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

#programming_dictionary = {}

programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

# Loop through a Dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

#########################################################
# Exercise 1 - Grading Program

# Score 91 - 100: Grade = "Outstanding"
# Score 81 - 90: Grade = "Exceeds Expectations"
# Score 71 - 80: Grade = "Acceptable" 
# Score 70 or lower: Grade = "Fail"

student_scores = {
    "Harry" : 81, 
    "Ron" : 78,
    "Hermione" : 99,
    "Draco" : 74,
    "Neville" : 62,
}

student_grades = {}

for students in student_scores:
    score = student_scores[students]
    if score > 91:
        student_grades[students] = "Outstanding"
    elif score > 81 and score < 90:
        student_grades[students] = "Exceeds Expectations"
    elif score > 71 and score < 80:
        student_grades[students] = "Acceptable"
    else:
        student_grades[students] = "Fail"

print(student_grades)


#########################################################
# NESTING
# Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijion"],
    "Germany": ["Berlin", "Hamburg", "Struttgart"]
} 

# Nesting a Dictionary in a Dictionary
travel_log = {
    "France": {"Cities Visited": ["Paris", "Lille", "Dijion"]}, "No of visits": 6,
    "Germany": {"Cities Visited": ["Paris", "Lille", "Dijion"], "No of visits": 3},
}

# Nesting a dictionary in a List
travel_log = [
 {
    "Country": "France", 
    "Cities Visited": ["Paris", "Lille", "Dijion"], 
    "No of visits": 6
 },
 {
    "Country": "Germany", 
    "Cities Visited": ["Paris", "Lille", "Dijion"], 
    "No of visits": 3
 },
]

# Exercise 2 - Adding a dictionay to a list

# Instruction:
# 1. Add Russia to list
# 2. Cities visited - Moscow and Saint Petersburg
# 3. No of visits - 2

travel_log = [
 {
    "Country": "France", 
    "Cities Visited": ["Paris", "Lille", "Dijion"], 
    "Visits": 6
 },
 {
    "Country": "Germany", 
    "Cities Visited": ["Paris", "Lille", "Dijion"], 
    "Visits": 3
 },
]

New_dict = [
 {
    "Country": "Russia",
    "Cities Visited": ["Moscow", "Saint Petersburg"], 
    "Visits": 2
 }
]

travel_log.append(New_dict)

print(travel_log)


# Attempting above exercise in a different way
travel_log = [
 {
    "Country": "France", 
    "Cities_Visited": ["Paris", "Lille", "Dijion"], 
    "Visits": 6
 },
 {
    "Country": "Germany", 
    "Cities_Visited": ["Paris", "Lille", "Dijion"], 
    "Visits": 3
 },
]

def new_country(Country, Cities_Visited, Visits):
    new_country = {}
    new_country['country'] = Country
    new_country['cities'] = Cities_Visited
    new_country['visits'] = Visits
    travel_log.append(new_country)

new_country("Russia", ["Moscow", "Saint Petersburg"], 2)
print(travel_log)


# Attempting above exercise in a different way
travel_log = [
 {
    "Country": "France", 
    "Cities_Visited": ["Paris", "Lille", "Dijion"], 
    "Visits": 6
 },
 {
    "Country": "Germany", 
    "Cities_Visited": ["Paris", "Lille", "Dijion"], 
    "Visits": 3
 },
]

travel_log +=  [
 {
    "Country": "Russia", 
    "Cities_Visited": ["Moscow", "Saint Petersburg"], 
    "Visits": 2
 }
]

print(travel_log)


##########################################################
# Final Exercise - Online Biding
from clear import clear

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()

