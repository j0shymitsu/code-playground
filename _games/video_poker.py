import math
import random



###################
### VIDEO POKER ###
###################



# Define constants

card_ranks = ['2','3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
card_suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
hand_ranks = {
    'Royal Flush' : 1, 
    'Straight Flush' : 2, 
    'Four of a Kind' : 3, 
    'Full House' : 4, 
    'Flush' : 5, 
    'Straight' : 6, 
    'Three of a Kind' : 7, 
    'Two pair' : 8, 
    'Jacks or Better' : 9, 
    'Nothing' : 10, 
}
payout_table = {        # Stolen from mobilots lmao
    'Royal Flush' : 250, 
    'Straight Flush' : 50, 
    'Four of a Kind' : 25, 
    'Full House' : 9, 
    'Flush' : 6, 
    'Straight' : 4, 
    'Three of a Kind' : 3, 
    'Two pair' : 2, 
    'Jacks or Better' : 1, 
}

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} of {self.suit}'
    
class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in card_ranks for suit in card_suits]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_cards):
        return [self.cards.pop() for _ in range(num_cards)]

deck = Deck()
deal = deck.deal(5)

for card in deal:
    print(card)


# Card/deck management

# Hands

# Game loop