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

    def deal_card(self):
        return self.all_cards.pop(0)


class Player:

    def __init__(self, name, bankroll=500):
        self.name = name
        self.bankroll = bankroll

    def __str__(self):
        return f'{self.name} currently has {self.bankroll} in their bankroll.'

    
class Hand:

    def __init__(self):

        self.card_list = []
        self.value = 0
        self.num_aces = 0

    def __str__(self):

        card_string = ""

        for card in self.card_list:
            card_string += str(card) + "   "

        return card_string

    def add_card(self, card):

        self.card_list.append(card)

        if card.rank == "Ace":

            if self.value > 10:
                self.value += card.value[0]
            else:
                self.value += card.value[1]
                self.num_aces += 1
        else:
            self.value += card.value
        
        if self.num_aces > 0 and self.value > 21:
            self.num_aces -= 1
            self.value -= 10


def play_again(current_bankroll):
    
    if current_bankroll == 0:
        print("Sorry, you have no money left to play.")
        return False
    
    decision = input("Would you like to play again? (Y/N): ")

    if decision == 'Y':
        return True
    elif decision == 'N':
        return False
    else:
        print("Invalid input. Please try again.")
        play_again(current_bankroll)


player1 = Player("Sam")
game_on = True

print(f"Welcome to Black Jack {player1.name}!")
input("Press enter to start the game.")


while game_on:

    player_turn = True
    betting_turn = True
    player_busted = False
    new_deck = Deck()
    new_deck.shuffle_deck()
    dealer_hand = Hand()
    player_hand = Hand()

    while betting_turn:
        try:
            player_bet = int(input(f"Please place your bets (1-{player1.bankroll}): "))
        except:

            print(f'Please only enter an integer between 1 and {player1.bankroll}\n\n')
            continue
        else:

            if player_bet > player1.bankroll:
                print("You don't have enough money to place a bet of that size! Please try again!\n\n")
            else:

                player1.bankroll -= player_bet
                betting_turn = False

    for _ in range(2):

        dealer_hand.add_card(new_deck.deal_card())
        player_hand.add_card(new_deck.deal_card())

    while player_turn:

        print("\n\n")
        print(f"Dealer's Hand: {dealer_hand.card_list[0]}   *Face Down*")
        print("")
        print(f'Your Hand: {player_hand}')
        print(f'Current Value: {player_hand.value}')

        
        try:
            option = int(input("Would you like to (1) Hit or (2) Stay (Input 1 or 2): "))
        except:

            print("Invalid selection! Please input only 1 or 2.")
            continue
        else:

            if option == 1:

                player_hand.add_card(new_deck.deal_card())

                if player_hand.value > 21:

                    player_busted = True
                    player_turn = False
                    print(f'Your Hand: {player_hand}')
                    print(f'Current Value: {player_hand.value}')
                    print("Sorry! You busted this hand!")
                    break
                else:
                    continue

            elif option == 2:

                print(f"Your final hand value is: {player_hand.value}")
                player_turn = False
            else:

                print("Invalid selection! Please input only 1 or 2.")
                continue

    if player_busted:

        print(f"You lost a total of {player_bet} this hand.")
        game_on = play_again(player1.bankroll)
    else:

        while dealer_hand.value < 21 and dealer_hand.value < player_hand.value:
            dealer_hand.add_card(new_deck.deal_card())
            print("\n\n")
            print(f"Dealer's Hand: {dealer_hand}")
            print(f"Dealer's Value: {dealer_hand.value}")
            print(f'Your Final Value: {player_hand.value}')

        if player_hand.value > dealer_hand.value < 21:

            print(f"You beat the dealer! Congratulations you have earned {player_bet * 2} dollars!")
            player1.bankroll += player_bet * 2
            game_on = play_again(player1.bankroll)
        elif player_hand.value < dealer_hand.value < 21:

            print(f'You lost this hand. Your bet of {player_bet} goes to the house.')
            game_on = play_again(player1.bankroll)
        else:

            print(f"The dealer has busted! Congratulations you have earned {player_bet * 2} dollars!")
            player1.bankroll += player_bet * 2
            game_on = play_again(player1.bankroll)
        

