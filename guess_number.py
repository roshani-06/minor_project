import random

EASY_TURNS = 10
HARD_TURNS = 5

def check_result(guess_number, chose_number, turns):
    if guess_number > chose_number:
        print("Too high.")
    elif guess_number < chose_number:
        print("Too low.")
    else:
        print(f"You guessed the correct number {chose_number}")
        return turns
    return turns - 1

def check_difficulty():
    level = input("Choose difficulty. Type 'easy' or 'hard':")
    if level == "easy":
        return EASY_TURNS
    else:
        return HARD_TURNS

def game():
    print("Welcome to the Guess Number")
    print("I am thinking of a number between 1 and 100")
    chose_number = random.randint(1, 100)
    print(chose_number)
    turns = check_difficulty()
    guess = 0
    while guess != chose_number:
        print(f"You have {turns} guesses left")
        guess_number = int(input("Guess the number: "))
        guess = guess_number
        turns = check_result(guess_number, chose_number, turns)
        if guess == chose_number:
            return
        if turns == 0:
            print("You lose, ran out of guesses")
            return
        else:
            print("Guess again")

game()






