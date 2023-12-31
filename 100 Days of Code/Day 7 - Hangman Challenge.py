# Hangman Challenge
import random

word_list = ['Hangman', 'Wood', 'Max', 'Table', 'Huzaif']
chosen_word = random.choice(word_list)

display = ['-' for _ in chosen_word]  # Create the display with dashes

guesses = []  # Keep track of guessed letters
max_guesses = 6  # Set the maximum number of guesses

while '-' in display and max_guesses > 0:
   print(" ".join(display))  # Print the current display
   guess = input("Guess a letter: ").lower()

   if guess in guesses:
       print("You already guessed that letter. Try again.")
   elif guess in chosen_word:
       for i in range(len(chosen_word)):
           if chosen_word[i] == guess:
               display[i] = guess
   else:
       max_guesses -= 1
       print("Incorrect guess. You have", max_guesses, "guesses left.")
       guesses.append(guess)

if '-' not in display:
   print("You win! The word was", chosen_word)
else:
   print("You lose! The word was", chosen_word)
