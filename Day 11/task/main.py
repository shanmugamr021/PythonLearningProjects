from art import logo
from random import choice

def play_blackjack():
    want_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if want_play == 'y':
        player_option = 'y'
        print(logo)
        your_cards = [get_random_card(), get_random_card()]
        computer_cards = [get_random_card()]
        is_blackjack = check_blackjack(your_cards)
        if is_blackjack:
            final_score(your_cards, computer_cards, is_blackjack)
            play_blackjack()

        while player_option == 'y':
            print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")
            print(f"Computer's first card: {computer_cards[0]}")
            player_option = input("Type 'y' to get another card, type 'n' to pass:")
            if player_option == 'y':
                your_cards.append(get_random_card())
                if(sum(your_cards)) > 21:
                    break
            player_option_end(your_cards, computer_cards)
            play_blackjack()

def player_option_end(your_cards, computer_cards):
    add_remaining_computer_card(computer_cards)
    check_computer_blackjack = check_blackjack(computer_cards)
    if check_computer_blackjack:
        final_score(your_cards, computer_cards, False, check_computer_blackjack)

    final_score(your_cards, computer_cards, False, check_computer_blackjack)
    if sum(your_cards) > 21:
        print("You Lose")
    elif sum(computer_cards) > 21:
        print("You Won")
    elif sum(your_cards) > sum(computer_cards):
        print("You won")
    elif sum(your_cards) < sum(computer_cards):
        print("You Lose")
    else:
        print("It's a draw")

def add_remaining_computer_card(computer_cards):
    while sum(computer_cards) < 17:
        computer_cards.append(get_random_card())

def get_random_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return choice(cards)

def check_blackjack(your_cards):
    if len(your_cards) == 2:
        if 11 in your_cards and 10 in your_cards:
            return True
    return  False

def final_score(your_cards, computer_cards, is_blackjack, is_computer_blackjack):
    your_total = 0
    computer_score = 0
    if not is_blackjack:
        your_total = sum(your_cards)
        computer_score = sum(computer_cards)
    print(f"Your final hand: {your_cards}, final score: {your_total}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    result_blackjack_message(is_blackjack, is_computer_blackjack)

def result_blackjack_message(is_blackjack, is_computer_blackjack):
    if is_blackjack:
        print("Win with a BlackJack")

    if is_computer_blackjack:
        print("Computer Won with a BlackJack")


play_blackjack()