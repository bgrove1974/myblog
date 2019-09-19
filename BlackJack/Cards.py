# https://github.com/slott56/Mastering-Object-Oriented-Python-Second-Edition/blob/master/Chapter_10/ch10_ex2.py

from typing import List, Optional, Dict, Any
from enum import Enum


class Suit(str, Enum):
    Clubs = "♣"
    Diamonds = "♦"
    Hearts = "♥"
    Spades = "♠"


class Card:

    def __init__(self, rank: str, suit: Suit, hard: Optional[int]=None,
                 soft: Optional[int]=None) -> None:
        self.rank = rank
        self.suit = suit
        self.hard = hard or int(rank)
        self.soft = soft or int(rank)

    def __str__(self) -> str:
        return f"{self.rank!s}{self.suit.value!s}"


class AceCard(Card):

    def __init__(self, rank: str, suit: Suit) -> None:
        super().__init__(rank, suit, 1, 11)


class FaceCard(Card):

    def __init__(self, rank: str, suit: Suit) -> None:
        super().__init__(rank, suit, 10, 10)


__test__ = {name: value for name, value in locals().items()
            if name.startswith("test_")}


if __name__ == '__main__':

    import doctest

    doctest.testmod(verbose=False)
