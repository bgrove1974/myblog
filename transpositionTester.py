# https://inventwithpython.com/cracking/chapter9.html
# Transposition Cipher Test
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import random, sys, transpositionCipher, transpositionHacker

def main():
    # Set a random seed:
    random.seed(42)
    # Run 20 iterations of the tests:
    for i in range(20):
        # Generate random messages to test:
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)
        # Convert the message string to a list and shuffle it:
        message = list(message)
        random.shuffle(message)
