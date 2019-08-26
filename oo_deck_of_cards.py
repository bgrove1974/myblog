# Keeping it simple and following a blog post to start:
# https://medium.com/@anthonytapias/build-a-deck-of-cards-with-oo-python-c41913a744d3

######################################################
# There are three classes -- Card, Deck and Player.
# This card game doesn't do much more than demonstrate
# object oriented programming.
######################################################
import random


class Card:
    """
    Card takes 2 inputs: suit and value self.
    The attributes suit and value are set when a card object is created.
    To run the program in the terminal:

    -> python -i oo_deck_of_cards.py
    >> deck = Deck()
    >> deck.shuffle()
    >> ben = Player("Ben")
    >> ben.draw(deck)
    <__main__.Player instance at 0x105afa5f0>
    >> ben.showHand()
    11 of Diamonds
    >> ben.draw(deck)
    <__main__.Player instance at 0x105afa5f0>
    >> ben.showHand()
    11 of Diamonds
    9 of Diamonds
    """
    def __init__(self, suit, val):
        """
        Instantiate card object with value and suit.
        """
        self.suit = suit
        self.value = val

    def show(self):
        """
        Print card value and suit.
        """
        print("{} of {}".format(self.value, self.suit))


class Deck:
    """
    Build a deck of 52 cards with 4 suits.
    """
    def __init__(self):
        """
        Create an empty list and use a build method to populate our deck.
        """
        self.cards = []
        self.build()

    def build(self):
        """
        Outer loop through each suit, inner loop through range(1, 14).
        Then Card(suit, value) is appended to self.cards for a total of 52.
        """
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def show(self):
        "Shows all of the cards in the deck."
        for c in self.cards:
            c.show()

    def shuffle(self):
        """
        Shuffles the deck from back to front.
        Loop for i in (range(len(self.cards)) minus 1, which is the last
        element and we want to go to zero, 0, -1 decrement)
        Then pick a random index to the left of our current position, and swap
        cards r and i.
        """
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        """
        Draws a card from the shuffled deck using pop().
        """
        return self.cards.pop()


class Player:
    """
    Player has a name attribute and a hand attribute initialized as [].
    """
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        """
        Append Deck.drawCard() to self.hand and return the card drawn.
        """
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        """
        Loop through each card in self.hand and then show the card.
        """
        for card in self.hand:
            card.show()
