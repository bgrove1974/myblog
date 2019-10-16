# https://inventwithpython.com/cracking/chapter5.html
# Caesar Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import pyperclip

# The string to be encrypted/decrypted:
message = 'This is the secret message.'
# The encryption and decryption key:
key = 13
# Select whether the program encrypts or decrypts:
mode = 'encrypt' # or 'decrypt'
# Make a string including all symbols that our program will handle:
# Every possible symbol that can be encrypted:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
# Store the encrypted or decrypted form of the message:
translated = ''

# Only letters and symbols in the SYMBOLS string can be encrypted or decrypted.
for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)
        # Perform the encryption or decryption:
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key

        # Handle the wraparound, if necessary:
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        # Put it all together:
        translated = translated + SYMBOLS[translatedIndex]
    else:
        # Append the symbol as is, without encrypting or decrypting:
        translated = translated + symbol

# Output the translated string:
print()
print(translated)
print()
pyperclip.copy(translated)
