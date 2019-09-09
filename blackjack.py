# https://github.com/gsamarakoon/Fun-projects-for-Python/blob/master/A%20game%20of%20BlackJack.ipynb

# Basic blackjack game between player and dealer.


import random


# Variables needed for more than one class:
# suits: tuple, ranks: tuple, values: dict
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

# The game goes on while True:
playing = True

# Start with some playing cards:
class Card:
    """
    Create and assign playing card attributes suit and rank.
    """
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """
        String representation of the cards for the player to read.
        """
        return self.rank + ' of ' + self.suit


# Create the Deck as well as the shuffle and deal methods:
class Deck:
    """
    Represents a deck of playing cards for the blackjack game.
    """
    def __init__(self):
        """
        Initialize the deck by populating an empty list.
        """
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        """
        String representation that prints out the card objects.
        """
        # Begin with an empty string and append the cards:
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has ' + deck_comp

    def shuffle(self):
        """
        Shuffles the cards.
        """
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


# Create a hand:
class Hand:
    """
    Initialize the hand object as an empty list with value set to 0.
    An attribute is also added to keep track of the aces.
    """
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        """
        Deals a card.
        """
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces +=1

    def adjust_for_ace(self):
        """
        When you want the Ace to be 1 instead of 11.
        """
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


# Create a Chips class for betting on the cards.
class Chips:
