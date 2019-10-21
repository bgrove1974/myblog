# https://inventwithpython.com/cracking/chapter8.html
# Transposition Cipher Decryption
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import math, pyperclip

def main():
    myMessage = 'Cenoonommstmme oo snnio. s s c'
    myKey = 8
    plaintext = decryptMessage(myKey, myMessage)
    # Handle strings with spaces at the end:
    print(plaintext + '|')
    pyperclip.copy(plaintext)

def decryptMessage(key, message):
    """
    The transpositon decryption function will simulate the columns and rows of the grid that the plaintext is written on by using a list of strings.
    """
    # Calculate the number of columns in the grid:
    numOfColumns = int(math.ceil(len(message) / float(key)))
    # Calculate the number of rows:
    numOfRows = key
    # Calculate the number of 'shaded boxes' in the last column:
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    # Each string in plaintext represents a column in the grid:
    plaintext = [''] * numOfColumns
    # The column and row values point to the next character's location:
    column = 0
    row = 0
    for symbol in message:
        plaintext[column] += symbol
        # Point to the next column:
        column += 1
        # If we're out of columns or at a 'shaded box',
        # go back to the first column and next row:
        if (column == numOfColumns) or (column == numOfColumns -1 and row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1
    return ''.join(plaintext)

#  Call the main function if necessary:
if __name__ == '__main__':
    main()
