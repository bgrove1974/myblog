# https://inventwithpython.com/cracking/chapter7.html
# Transposition Cipher Encryption
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)
# Columnar transposition cipher
# https://en.wikipedia.org/wiki/Transposition_cipher

import pyperclip

def main():
    myMessage = 'Common sense is not so common.'
    myKey = 8
    ciphertext = encryptMessage(myKey, myMessage)
    # Add '|' in case there are spaces at the end of the encrypted message:
    print(ciphertext + '|')
    # Copy the encrypted string in ciphertext to the clipboard:
    pyperclip.copy(ciphertext)

def encryptMessage(key, message):
    """
    Each string in ciphertext represents a column in the grid.
    Continue looping through each column until currentIndex goes past the message length, then place the character at currentIndex in message at the end of the current column in the ciphertext list.
    Then move currentIndex over, repeat the process, and convert the ciphertext list into a single string value and return it.
    """
    ciphertext = [''] * key
    for column in range(key):
        currentIndex = column
        while currentIndex < len(message):
            ciphertext[column] += message[currentIndex]
            currentIndex += key
    return ''.join(ciphertext)

# Call the main function if transpositonCipher.py is run instead of being imported:
if __name__ == '__main__':
    main()
