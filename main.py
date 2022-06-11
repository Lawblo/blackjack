'''Handles game objects'''
from blackjack import Blackjack
from deck import Deck
from participants import Player
from participants import Dealer


deck = Deck()
deck.create_deck()
deck.shuffle_deck()
player1 = Player(deck, 'a')
player2 = Player(deck, 'b')
player3 = Player(deck, 'c')
player4 = Player(deck, 'd')
dealer = Dealer(deck)


player1.add_credits(100)
player2.add_credits(100)
# player3.add_credits(100)
game = Blackjack(deck, dealer, player1, player2, player3)
