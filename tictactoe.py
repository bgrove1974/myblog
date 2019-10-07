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
    return ((board[7] == letter and board[8] == letter and board[9] == letter)) or (board[4] == letter and board[5] == letter and board[6] == letter) or (board[1] == letter and board[2] == letter and board[3] == letter) or (board[7] == letter and board[4] == letter and board[1] == letter) or (board[8] == letter and board[5] == letter and board[2] == letter) or (board[9] == letter and board[6] == letter and board[3] == letter) or (board[7] == letter and board[5] == letter and board[3] == letter) or (board[9] == letter and board[5] == letter and board[1] == letter)

def getBoardCopy(board):
    """
    Make a copy of the board list and return it.
    """
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    """
    Make sure that the board space hasn't been taken already.
    """
    return board[move] == ' '

def getPlayerMove(board):
    """
    Allows the player to play their turn.
    """
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is you next move? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    """
    Returns a valid move from the passed list on the passed board.
    If the move is invalid, returns None.
    """
    possibleMoves = []
    for i in movesList:
        if is SpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    """
    Given a board and the computer's letter, determine the machine's next move.
    """
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter == 'X'

    # Now for the machine learning part -- our AI's strategy:

    # First, see if the machine can win on the next move:
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    # Next, see if the player can win on their next move and block them:
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    # After that, take one of the corners, if they're still free:
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Then take the center, if it's free:
    if isSpaceFree(board, 5):
        return 5

    # Last, choose a space on the sides:
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    """
    Return True if every space on the board is take, False otherwise.
    """
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

# Time to play the game!
print('Welcome to Tic-Tac-Toe!')
