# https://github.com/gsamarakoon/Fun-projects-for-Python/blob/master/A%20game%20of%20BlackJack.ipynb

# Basic blackjack game between player and dealer.


import random


# Variables needed for more than one class:
# suits: tuple, ranks: tuple, values: dict
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

# The game goes on while True:
playing = True

# Start with some playing cards:
class Card:
    """
    Create and assign playing card attributes suit and rank.
    """
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """
        String representation of the cards for the player to read.
        """
        return self.rank + ' of ' + self.suit


# Create the Deck as well as the shuffle and deal methods:
class Deck:
    """
    Represents a deck of playing cards for the blackjack game.
    """
    def __init__(self):
        """
        Initialize the deck by populating an empty list.
        """
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        """
        String representation that prints out the card objects.
        """
        # Begin with an empty string and append the cards:
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has ' + deck_comp

    def shuffle(self):
        """
        Shuffles the cards.
        """
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


# Create a hand:
class Hand:
    """
    Initialize the hand object as an empty list with value set to 0.
    An attribute is also added to keep track of the aces.
    """
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        """
        Deals a card.
        """
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces +=1

    def adjust_for_ace(self):
        """
        When you want the Ace to be 1 instead of 11.
        """
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


# Create a Chips class for betting on the cards.
class Chips:
    """
    Gaming chips for the player are initialized to 100.
    Also has methods for winning and losing bets.
    """
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


# Take bets:
def take_bet(chips):
    """
    This function contains the betting rules:
    bets have to be a whole number, and you can't bet chips you don't have.
    """
    while True:
        try:
            chips.bet = int(input("How many chips do you want to bet? "))
        except ValueError:
            print("Sorry, your bet must be an integer.")
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet cannot be more than {}."
                      .format(chips.total))
            else:
                break

# Add another card, aka hit:
def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

# Player's choice of hit or stand:
def hit_or_stand(deck, hand):
    """
    The player can hit or stand if it's their turn.
    When the variable playing is set to False, the dealer takes a turn.
    Anything the user enters other than 'h' or 's' prints a message.
    """
    global playing

    while True:
        x = input("Would you like to ('h')it or ('s')tand? ")

        if x[0].lower() == 'h':
            # Call the hit function defined above
            hit(deck, hand)

        elif x[0].lower() == 's':
            print("Player stands, Dealer's turn.")
            playing = False

        else:
            print("Sorry, please enter the 'h' or 's' key.")
            continue
        break

# Functions to display the cards:
def show_some(player, dealer):
    print("\nDealer's Hand")
    print("<card hidden>")
    print(" ", dealer.cards[1])
    print("\nPlayer's Hand: ", *player.cards, sep="\n")

def show_all(player, dealer):
    print("\nDealer's Hand: ", *dealer.cards, sep="\n")
    print("Dealer's Hand = ", dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep="\n")
    print("Player's Hand = ", player.value)

# Functions to handle game scenarios:
def player_busts(player, dealer, chips):
    print("Player Busts!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("Player Wins!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("Dealer Busts!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("Dealer Wins!")
    chips.lose_bet()

def push(player, dealer):
    print("Dealer ties player for a push.")

# Now for the game itself:
# GAMEPLAY #
while True:
    # Opening statement to greet the player:
    print()
    print("Welcome to BlackJack, let's play some cards!")
    print("Please bet between 1 and 100 chips.")

    # Create and shuffle the deck, then deal the cards:
    player_hand = Hand()
    deck = Deck()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Initialize the player's bank of chips:
    player_chips = Chips()

    # Prompt the player for their bet:
    take_bet(player_chips)

    # Show the player their cards and the dealer's up card:
    show_some(player_hand, dealer_hand)

    # Use playing variable from hit_or_stand function:
    while playing:
        # Prompt for player to hit or stand:
        hit_or_stand(deck, player_hand)
        # Reveal cards, except for the dealer's down card:
        show_some(player_hand, dealer_hand)
        # If player hits 21:
        if player_hand.value == 21:
            player_wins(player_hand, dealer_hand, player_chips)
        # If player goes over 21, call player_busts() and break the while loop:
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

        # If player doesn't bust, play until Dealer's hand reaches 17:
        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)
            # Reveal all cards:
            show_all(player_hand, dealer_hand)

        # Run different winning scenarios:
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        else:
            push(player_hand, dealer_hand)

    # Give the chip count:
    print("\nPlayer's winnings are at ", player_chips.total)

    # Ask for another game, and the player can continue or break:
    new_game = input("Another game of BlackJack? (Enter 'y' or 'n')")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break
