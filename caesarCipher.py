# https://inventwithpython.com/cracking/chapter5.html
# Caesar Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import pyperclip

# The string to be encrypted/decrypted:
message = 'This is the secret message. Shh.'
# The encryption and decryption key:
key = 13
# Select whether the program encrypts or decrypts:
mode = 'encrypt' # or 'decrypt'
# Make a string including all symbols that our program will handle:
# Every possible symbol that can be encrypted:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
# Store the encrypted or decrypted form of the message:
translated = ''
