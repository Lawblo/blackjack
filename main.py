import blackjack
from deck import Deck


class Participant:
    '''asdf'''
    def __init__(self):
        self.cards = []

    def get_card(self, deck):
        '''gets a card from the deck'''
        self.cards.append(deck.draw_card())

    def get_score(self):
        '''gets the score'''
        pass


class Player(Participant):
    '''Player specific actions'''
    pass


class Dealer(Participant):
    '''Dealer specific actions'''
    pass

a = Deck()
a.create_deck()
a.shuffle_deck()
b = Player()
b.get_card(a)
b.get_card(a)
blackjack.calculate_score(b.cards, Deck.CARD_VALUES)