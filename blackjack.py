# https://github.com/nachogentile/learn-python-with-blackjack/blob/master/blackjack.py
# Learning Python in the context of a blackjack game.

from random import random

# Make a list of the card colors:
card_colors = ["diamonds", "hearts", "spades", "clubs"]

# Make a Python dictionary to assign card values { str: int }:
card_value = {
    'A': 11,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10
}

def calculate_score(card_list):
    """
    Calculates the sum of the cards and compensates for the Ace.
    card_list: list of cards
    Returns:
        total: score of the list of cards.
    """
    total = 0
    for card in card_list:
        # Ace can be either 1 or 11:
        if total >= 11 and card == 'A':
            total += 1
        else:
            total += card_value[card]
    return total


def play_turn(deck):
    """
    One round of blackjack with player and dealer each taking a turn.
    deck: list of available cards
    Returns:
        Total score for the turn
    """
    # Store the cards that are dealt in a list:
    table_cards = []
    user_input = 'y'
    # Deal cards while user chooses 'y' and hasn't busted:
    while user_input == 'y':
        # Calculate a random position for the card:
        position = int(random() * len(deck))
        # Deal the card:
        print(deck[position])
        table_cards.append(deck[position][0])
        # Make sure you don't keep dealing the same card:
        del deck[position]
        # If player busts (goes over 21), break out of the loop:
        if calculate_score(table_cards) >= 21:
            break
        # Ask the user if they want another card:
        user_input = raw_input("Do you want another card? (enter 'y') ")
    # Print player's score:
    print "Your score is %d" % calculate_score(table_cards)
    # Return the total score for the round:
    return calcualte_score(table_cards)
