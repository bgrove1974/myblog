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
    board = []
    for i in range(WIDTH):
        board.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    return board

def isValidMove(board, tile, xstart, ystart):
    """
    Return False if the player's move on xstart, ystart is invalid.
    Otherwise, return a list of spaces that the player would take over.
    """
    if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
        return False

    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'

    tilesToFlip = []
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1],[0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        # First step in the x direction:
        x += xdirection
        # First step in the y direction:
        y += ydirection
        while isOnBoard(x, y) and board[x][y] == otherTile:
            # Keep moving in this x & y direction:
            x += xdirection
            y += ydirection
            if isOnBoard(x, y) and board[x][y] == tile:
            # There are pieces to flip over.
            # Go in the reverse direction until we reach the original space.
            while True:
                x -= xdirection
                y -= ydirection
                if x == xstart and y == ystart:
                    break
                tilesToFlip.append([x, y])
    if len(tilesToFlip) == 0:
        # If no tiles were flipped, then this move is invalid.
        return False
    return tilesToFlip

def isOnBoard(x, y):
    pass
