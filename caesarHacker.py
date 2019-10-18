# https://inventwithpython.com/cracking/chapter6.html
# Caesar Cipher Hacker
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Loop through every possible key:
print()
print('The possible encryptions are: ')
print()
for key in range(len(SYMBOLS)):
    # Set translated to a blank string so previous translations are erased:
    translated = ''
    # Loop through each symbol in the message:
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex = key
            # Handle strings that wraparound:
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)
            # Append the decrypted symbol:
            translated = translated + SYMBOLS[translatedIndex]
        else:
            # Append the symbol without any transformation:
            translated = translated + symbol
    # Display the possible encryptions:
    print('Key #%s: %s' %(key, translated))
print()
