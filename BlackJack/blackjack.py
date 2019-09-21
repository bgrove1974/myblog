# http://buildingskills.itmaybeahack.com/book/oodesign-3.1/html/finish/python_testing.html

# Our initial Card class needs to have just enough of an API
# to allow the tests to run.
# Here’s our skeleton Card class:

import sys


class Card:
    Clubs = u'\N{BLACK CLUB SUIT}'
    Diamonds = u'\N{WHITE DIAMOND SUIT}'
    Hearts = u'\N{WHITE HEART SUIT}'
    Spades = u'\N{BLACK SPADE SUIT}'
    Jack = 11
    Queen = 12
    King = 13
    Ace = 1

    def __init__(self, rank, suit):
        assert suit in (Card.Clubs, Card.Diamonds, Card.Hearts, Card.Spades)
        assert 1 <= rank < 14
        self.rank = rank
        self.suit = suit
        self.order = rank
