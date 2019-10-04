# Tic-Tac-Toe
# https://inventwithpython.com/invent4thed/chapter10.html

import random

def drawBoard(board):
    """
    board -> list of 10 strings representing the board
    This function ignores index 0 and prints out the playing board.
    """
    print(board[7], + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4], + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1], + '|' + board[2] + '|' + board[3])

def inputPlayerLetter():
    """
    Player can choose X or O.
    Returns a list with the player's letter as the first item and the computer's letter as the second.
    """
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print("Do you want to be X or O?")
        letter = input().upper
    # List element 0 is the player's letter, list element 1 is the computer's.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    """
    Randomly choose who goes first.
    """
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(board, letter):
    """
    Given a board and a player's letter as input.
    Returns True if that player has won.
    """
            # Across the top:
    return ((board[7] == letter and board[8] == letter and board[9] == letter))
            # Across the middle:
        or (board[4] == letter and board[5] == letter and board[6] == letter)
            # Across the bottom:
        or (board[1] == letter and board[2] == letter and board[3] == letter)
            # Down the left side:
        or (board[7] == letter and board[4] == letter and board[1] == letter)
            # Down the middle
        or (board[8] == letter and board[5] == letter and board[2] == letter)
            # Down the right side:
        or (board[9] == letter and board[6] == letter and board[3] == letter)
            # Diagonal
        or (board[7] == letter and board[5] == letter and board[3] == letter)
            # Diagonal
        or (board[9] == letter and board[5] == letter and board[1] == letter)

def getBoardCopy(board):
    """
    Make a copy of the board list and return it.
    """
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy
