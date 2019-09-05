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


class Hist(dict):
    """
    A map from each item (x) to its frequency.
    """
    def __init__(self, seq = []):
        """
        Creates a new histogram starting with the items in seq.
        """
        for x in seq:
            self.count(x)

    def count(self, x, f=1):
        """
        Increments or decrements the counter associated with item (x).
        """
        self[x] = self.get(x, 0) + f
        if self[x] == 0:
            del self[x]


class PokerHand(Hand):
    """
    Represents a poker hand.
    """
    all_labels = ['straightflush', 'fourkind', 'fullhouse', 'flush',
                  'straight', 'threekind', 'twopair', 'pair', 'highcard']

    def make_histograms(self):
        """
        Computes histograms for suits and hands.
        Creates the following attributes:
            suits: a histogram of the suits in the hand.
            ranks: a histogram of the ranks.
            sets:  a sorted list of the rank sets in the hand.
        """
        self.suits = Hist()
        self.ranks = Hist()

        for c in self.cards:
            self.suits.count(c.suit)
            self.ranks.count(c.rank)

        self.sets = list(self.ranks.values())
        self.sets.sort(reverse=True)

    def has_highcard(self):
        """
        Returns True if this hand has a high card.
        """
        return len(self.cards)

    def check_sets(self, *t):
        """
        Checks whether self.sets contains sets that are at least as big as the
        requirements in t.
        t: list of int
        """
        for need, have in zip(t, self.sets):
            if need > have:
                return False
        return True

    def has_pair(self):
        """
        Checks whether this hand has a pair.
        """
        return self.check_sets(2)

    def has_twopair(self):
        """
        Checks whether this hand has two pair.
        """
        return self.check_sets(2, 2)

    def has_threekind(self):
        """
        Checks whether this hand has three of a kind.
        """
        return self.check_sets(3)

    def has_fourkind(self):
        """
        Checks whether this hand has four of a kind.
        """
        return self.check_sets(4)

    def has_fullhouse(self):
        """
        Checks whether this hand has a full house.
        """
        return self.check_sets(3, 2)

    def has_flush(self):
        """
        Checks whether this hand has a flush.
        """
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_straight(self):
        """
        Checks whether this hand has a straight.
        """
        # Make a copy of the rank histogram:
        ranks = self.ranks.copy()
        ranks[14] = ranks.get(1, 0)
        # See if we have five in a row:
        return self.in_a_row(ranks, 5)

    def in_a_row(self, ranks, n=5):
        """
        Checks whether the histogram has n ranks in a row.
        hist: map from rank to frequency
        n: number we need to get to
        """
        count = 0
        for i in range(1, 15):
            if ranks.get(i, 0):
                count += 1
                if count == n:
                    return True
            else:
                count = 0
        return False

    def has_straightflush(self):
        """
        Checks whether this hand has a straight flush.
        This algorithm partitions the hand by suit and checks each sub-hand for
        a flush, and then each partitioned hand is checked for a straight.
        """
        d = {}
        for c in self.cards:
            d.setdefault(c.suit, PokerHand()).add_card(c)
        for hand in d.values():
            if len(hand.cards) < 5:
                continue
            hand.make_histograms()
            if hand.has_straight():
                return True
        return False

    def classify(self):
        """
        Classifies the hand and creates the labels attribute.
        """
        self.make_histograms()
        self.labels = []
        for label in PokerHand.all_labels:
            f = getattr(self, 'has_' + label)
            if f():
                self.labels.append(label)


if __name__ == '__main__':
    # Deal a deck:
    deck = Deck()
    deck.shuffle()

    # Deal hands of cards (from a single deck) and classify them:
    for i in range(10):
        # Keep the total number of cards dealt less than 52
        hand = PokerHand()
        deck.move_cards(hand, 5)
        hand.sort()
        print(hand)
        print(hand.has_flush())
        print('')
