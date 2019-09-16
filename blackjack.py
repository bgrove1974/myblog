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
