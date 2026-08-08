import random

def deal_card():
    """return the random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10 ,10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """take the list of cards and return the score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Match draw"
    if c_score == 0:
        return "Lose, dealer has Blackjack"
    elif u_score == 0:
        return "You win with blackjack"
    elif c_score > 21:
        return "Dealer win"
    elif u_score > 21:
        return "You lose"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"


def play_game():
    user_card = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score =  calculate_score(user_card)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_card}, current score: {user_score}")
        print(f"Computer first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("type 'y' to take another card or type 'n' to pass ")
            if user_should_deal == "y":
                user_card.append(deal_card())
            else:
                is_game_over = True

    while  computer_score != 0 and computer_score < 17:
        user_card.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_card}, final score: {user_score}")
    print(f"Computer's final card: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play again? (y/n): ").lower() == "y":
    print("\n" *20)
    play_game()

