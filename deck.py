'''module handles game deck'''
import random


class Deck:
    '''Handles the deck of cards'''

    CARD_COLORS = {
        'diamonds': '\u2662',
        'cloves': '\u2663',
        'spades': '\u2664',
        'hearts': '\u2665'
    }

    CARD_VALUES = {
        'A': 11,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10
    }

    def __init__(self) -> None:
        self.deck = []

    # def __str__(self) -> str:
    #     return f'Deck has {len(self.deck)} cards left'

    def create_deck(self) -> list:
        '''build the deck'''
        new_deck = []
        for symbol in self.CARD_COLORS.values():
            for name, value in self.CARD_VALUES.items():
                new_deck.append([name, symbol, value])
        self.deck = new_deck
        return self.deck

    def add_deck(self, *args: list) -> list:
        '''combine several decks'''
        for arg in args:
            self.deck.extend(arg)
        return self.deck

    def shuffle_deck(self) -> list:
        '''shuffle deck'''
        random.shuffle(self.deck)
        return self.deck

    def draw_card(self):
        '''hands off a random card from the deck'''
        return self.deck.pop()
