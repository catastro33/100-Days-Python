# Hangman Project
import random
end_game = False
word_list = ['Hangman', 'Wood', 'Max', 'Table', 'Huzaif']

chosen_word = random.choice(word_list)
print(chosen_word)

display = []
for letter in chosen_word:
    display += '-'
print(display)


while not end_game:
    guess = input("Guess a letter\n").lower()

    for position in range(len(chosen_word)):
        if letter == chosen_word[position]:
            display[position] = letter

    print(display)
    
    if '-' not in display:
        end_game = True
        print("You win.")
        


    