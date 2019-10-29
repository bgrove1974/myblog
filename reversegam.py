# Reversegam: a clone of Othello/Reversi

import random
import sys

# Global variables for an 8 x 8 board:
WIDTH = 8
HEIGHT = 8

def drawBoard(board):
    """
    Print the board passed to this function.
    Returns a None value.
    """
    print('  12345678')
    print(' +--------+')
    for y in range(HEIGHT):
        print('%s|' % (y+1), end='')
        for x in range(WIDTH):
            print(board[x][y], end='')
        print('|%s' % (y+1))
    print(' +--------+')
    print('  12345678')

def getNewBoard():
    """
    Create a brand-new blank board data structure.
    """
