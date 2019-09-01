"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from Card import Hand, Deck


class PokerHand(Hand):
    """
    Represents a poker hand.
    """

    def suit_hist(self):
        """
        Builds a histogram of the suits that appear in the hand.
        The results are stored in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def has_flush(self):
        """
        Returns True if the hand has a flush, False otherwise.
        This method works for hands with 5 cards or more.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False


if __name__ == '__main__':
    # Deal a deck:
    deck = Deck()
    deck.shuffle()

    # Deal seven hands of cards and classify them:
    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print(hand)
        print(hand.has_flush())
        print('')
