import random
from hangman_words import word_list
from hangman_art import stages

lives = 6

chosen_word = random.choice(word_list)

placeholder =""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder+= "_"
print(placeholder)

game_over = False
correct_list = []

while not game_over:
    Guess = input("Guess a letter:").lower()

    display = ""
    for letter in chosen_word:
        if letter == Guess:
            display += letter
            correct_list.append(letter)
        elif letter in correct_list:
            display += letter
        else:
            display += "_"
    print(display)

    if Guess not in chosen_word:
        lives -= 1
        if lives ==0:
            game_over = True
            print("You Lose!")

    if "_" not in display:
        game_over = True
        print("you win")

    print(stages[lives])