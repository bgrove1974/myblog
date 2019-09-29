# http://web.cs.iastate.edu/~adisak/datascience/Python%20book/chapter18/

################################################################################
# Craps is played like this. Each round of the game has two "phases":
# In the first phase, you roll the dice once.
# If the result is 7 or 11, you win immediately and the round ends.
# If the result is 2, 3, or 12, you lose immediately, and the round ends.
# In all other cases the number you roll (which has to be a 4, 5, 6, 8, 9,
# or 10) is called the "point", and you go on to the second phase.
# In the second phase you keep rolling the dice until you roll a 7 or you roll
# the value of the "point" from the previous phase.
# If you roll a 7 first, you lose, and if you roll the point first, you win.
# The payoff for the bets is always one-to-one: if you bet $10 and win,
# the bank gives you $10.
################################################################################

import random


def roll_dice():
    """
    Simulates the rolling of two dice.
    Returns an integer between 2 and 12.
    """
    input("Press ENTER/RETURN to roll the dice... ")
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    print()
    print("Die 1: ", a)
    print("Die 2: ", b)
    print()
    return a + b
roll = roll_dice()

def play_one_round(bet):
    """
    Plays one round of craps using the given amount as the bet.
    Returns amount won as positive, amount lost as negative.
    """
    roll = roll_dice()

    # First phase: 7 or 11 wins, 2, 3, or 12 loses.
    if roll == 7 or roll == 11:
        print("You Win!")
        return bet
    elif roll == 2 or roll == 3 or roll == 12:
        print("You Lose.")
        return -bet
    else:
        point = roll
        print()
        print ("The point is now", point, ".")

    # Second phase:
    

play_one_round(1000)
