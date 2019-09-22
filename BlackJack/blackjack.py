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

    @property
    def hardValue(self):
        return self.rank

    @property
    def softValue(self):
        return self.rank

    def __repr__(self):
        return "{class_}({rank!r},{suit!r})".format(
            class_ = type(self).__name__, **vars(self)
        )

    def __str__(self):
        return "{rank:2d}{suit}".format_map(vars(self))

    @property
    def image(self):
        s = {Card.Spades:0x1F0A0, Card.Hearts:0x1F0B0, Card.Diamonds:0x1F0C0,
             Card.Clubs:0x1F0D0}[self.suit]
        r = self.rank if self.rank < 12 else self.rank+1
        return chr(s+r)

    def __le__(self, other):
        return self.order <= other.order

    def __lt__(self, other):
        return self.order < other.order

    def __ge__(self, other):
        return self.order >= other.order

    def __gt__(self, other):
        return self.order > other.order

    def __eq__(self, other):
        return self.order == other.order

    def __ne__(self, other):
        return self.order != other.order

    def __hash__(self):
        return (hash(self.rank) + hash(self.suit))%sys.hash_info.width
