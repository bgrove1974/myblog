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
