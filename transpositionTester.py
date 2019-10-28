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
        # Convert the list back into a string:
        message = ''.join(message)

        print('Test #%s: "%s..."' % (i + 1, message[:50]))

        # Check all possible keys for each message:
        for key in range(1, int(len(message)/2)):
            encrypted = transpositionCipher.encryptMessage(key, message)
            decrypted = transpositionHacker.decryptMessage(key, encrypted)
            # If message and decrypted don't match, throw an error and quit:
            if message != decrypted:
                print('Mismatch with key %s and message %s.' % (key, message))
                print('Decrypted is: ' + decrypted)
                sys.exit()

    print('Transpostion Cipher test passed')

# Call the main function if necessary:
if __name__ == '__main__':
    main()
