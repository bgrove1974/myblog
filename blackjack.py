# https://gist.github.com/saulcosta/13909e2e51f94ff7b37700c74b885ab6

import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return " of ".join((self.value, self.suit))


class Deck:
    def __init__(self):
        self.cards = [Card(s, v) for s in ["Spades", "Clubs",
                                           "Hearts", "Diamonds"]
                     for v in ["A", "2", "3", "4", "5", "6", "7",
                               "8", "9", "10", "J", "Q", "K"]]

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)
