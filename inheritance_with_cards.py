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
