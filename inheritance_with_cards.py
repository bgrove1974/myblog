"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import random


class Card:
    """
    Represents a playing card.
    Attributes:
        suit : integer 0-3
            Spades   -> 3
            Hearts   -> 2
            Diamonds -> 1
            Clubs    -> 0
        rank : integer 1-13
            Jack  -> 11
            Queen -> 12
            King  -> 13
    """

    # Assign class attributes:
    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "Jack", "Queen", "King"]
    # The first element of rank_names is None because there is no rank zero.
    # Using None as a place-keeper, index 2 maps to the string '2', and so on.
    # To avoid this tweak, we could have used a dictionary instead of a list.

    def __init__(self, suit=0, rank=2):
        """
        Default card is 2 of Clubs.
        To create a Card, call Card(suit, rank).
        >> queen_of_diamonds = Card(1,12)
        """
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """
        String representation to print the cards.
        >> card1 = Card(2, 11)
        >> print(card1)
        Jack of Hearts
        """
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __lt__(self, other):
        """
        Less-than method is used to compare suits, Clubs being the lowest.
        If suits are equal, rank is used.
        """
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2


class Deck:
    """
    Generates a standard deck of 52 playing cards.
    """

    def __init__(self):
        """
        Use a nested loop to populate the deck.
        """
        self.cards = []
        for suit in range(4):
            # Don't start at index 0
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        """
        String representation of our deck for the players and dealers to read.
        Returns a single string on 52 lines.

        >> deck = Deck()
        >> print(deck)
        Ace of Clubs
        2 of Clubs
        3 of Clubs
        ...
        ...
        Jack of Spades
        Queen of Spades
        King of Spades
        """
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
