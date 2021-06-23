'''
Interactive black jack game. One computer dealer and one human player. Human player will have a starting bankroll.
The player places a bet and then cards are dealt. One dealer card will be face up (the other face down).
Player has option of either 'hit' or 'stay'. If player goes over 21 dealer wins. If player stays, dealer will hit
until they beat player or bust. If player wins their bet gets doubled.
'''
from random import shuffle


# Global variables
suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":10, "Queen":10, "King":10, "Ace":[1, 11]}

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))
    
    def shuffle_deck(self):
        shuffle(self.all_cards)


