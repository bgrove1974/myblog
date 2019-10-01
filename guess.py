# https://inventwithpython.com/invent4thed/chapter3.html

## Guess the number game

import random

guessesTaken = 0

print("Please enter your name.")
myName = input()

number = random .randint(1, 20)
print(myName,", please choose a number between 1 and 20.")

for guessesTaken in range(6):
    
