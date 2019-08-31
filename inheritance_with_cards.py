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

    def __eq__(self, other):
        """
        Checks whether self and other have the same rank and suit.
        Returns a boolean.
        """
        return self.suit == other.suit and self.rank == other.rank

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
    Attributes are a list of Card objects named cards.
    """

    def __init__(self):
        """
        Use a nested loop to populate the deck with 52 cards.
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

    def pop_card(self, i=-1):
        """
        Deals from the bottom of the deck.
        """
        return self.cards.pop(i)

    def add_card(self, card):
        """
        Veneer method that adds a card.
        """
        self.cards.append(card)

    def remove_card(self, card):
        """
        Removes a card from the deck or raises an exception if it's not there.
        """
        self.cards.remove(card)

    def shuffle(self):
        """
        Pseudorandomly shuffle the cards.
        """
        random.shuffle(self.cards)

    def sort(self):
        """
        Sorts the cards lowest to highest.
        """
        self.cards.sort()

    def move_cards(self, hand, num):
        """
        The pop_card and add_card methods are encapsulated in this method.
        move_cards has two arguments: Hand object and number of cards to deal.
        It modifies both self and hand, and returns None.
        In some games, cards are moved from one hand to another, or from a hand back to the deck.
        You can use move_cards for any of these operations.
        self can be either a Deck or a Hand, and hand, despite the name, can also be a Deck.
        """
        for i in range(num):
            hand.add_card(self.pop_card())


class Hand(Deck):
    """
    Represents a hand of playing cards.
    Inherits methods like pop_card and add_card from the Deck class.
    """

    def __init__(self, label=''):
        """
        Initialize the cards variable to an empty list.

        % python3 -i inheritance_with_cards.py
        >> hand = Hand('some hand')
        >> hand.cards
        []
        >> hand.label
        'some hand'
        >>
        """
        self.cards = []
        self.label = label


#################################
# Any time you are unsure about the flow of execution through your program,
# the simplest solution is to add print statements at the beginning of the
# relevant methods.
# If Deck.shuffle prints a message that says something like Running
# Deck.shuffle, then as the program runs it traces the flow of execution.
# As an alternative, you could use this function, which takes an object and
# a method name (as a string) and returns the class that provides the
# definition of the method:
def find_defining_class(obj, method_name):
    """
    obj -> str
    meth_name -> str
    % python3 -i inheritance_with_cards.py
    >> hand = Hand()
    >> find_defining_class(hand, 'shuffle')
    <class '__main__.Deck'>
    >>
    The shuffle method for this Hand is the one in Deck
    """
    for ty in type(obj).mro():
        # https://stackoverflow.com/questions/2010692/what-does-mro-do
        # https://docs.python.org/3/library/stdtypes.html#class.__mro__
        if method_name in ty.__dict__:
            return ty
    return None


if __name__ == '__main__':
    # Deals a five-card hand that is printed to the terminal.
    deck = Deck()
    deck.shuffle()

    hand = Hand()
    print(find_defining_class(hand, 'shuffle'))

    deck.move_cards(hand, 5)
    hand.sort()
    print(hand)
