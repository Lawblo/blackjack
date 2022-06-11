'''handles participants'''
import json


class Participant:
    '''asdf'''
    def __init__(self, deck):
        self.cards = []
        self.get_card(deck)
        self.get_card(deck)

    def get_card(self, deck):
        '''draw a card from the deck'''
        self.cards.append(deck.draw_card())

    def get_score(self, game):
        '''gets the participants hand value'''
        return game.calculate_score(self.cards)


class Player(Participant):
    '''Player specific actions'''
    def __init__(self, deck, name):
        super().__init__(deck)
        self.name = name
        self.play_credits = 0
        self.games_won = 0
        self.games_lost = 0
        self.games_drawn = 0

    def save_player(self):
        '''save playerdata to file'''
        fhand = open(
            f'data/players/player_{self.name}.JSON', 'w', encoding='UTF-8'
            )
        player = {
            "name": self.name,
            "play_credits": self.play_credits,
            "games_won": self.games_won,
            "games_lost": self.games_lost,
            "games_drawn": self.games_drawn,
        }
        store = json.dumps(player)
        fhand.write(store)
        fhand.close()

    def load_player(self):
        '''read playerdata from file'''
        fhand = open(
            f'data/players/player_{self.name}.JSON', 'r', encoding='UTF-8'
            )
        player = json.load(fhand)
        fhand.close()
        self.name = player['name']
        self.play_credits = player['play_credits']
        self.games_won = player['games_won']
        self.games_lost = player['games_lost']
        self.games_drawn = player['games_drawn']

    @property
    def win_rate(self):
        '''win rate'''
        return self.games_won / self.games_played

    @property
    def loss_rate(self):
        '''loss rate'''
        return self.games_lost / self.games_played

    @property
    def games_played(self):
        '''computes total games'''
        return self.games_won + self.games_lost + self.games_drawn

    def __str__(self) -> str:
        return_string = f'{" Player " + self.name + " ":_^30}\n'
        return_string += f'Credits: {self.play_credits:>21}\n'
        # return_string += f'Games played: {self.games_played:>16}\n'
        # return_string += f'Wins: {self.games_won:>24}\n'
        # return_string += f'Losses: {self.games_lost:>22}\n'
        return_string += f'{"-"*30}'

        return return_string

    def add_credits(self, play_credits):
        '''add credits to play with'''
        self.play_credits += play_credits
        # print(f'Player {self.name} added {play_credits} credits.')
        # print('Total credits: ', play_credits)
        return True

    def get_credits(self):
        '''get player credits'''
        # print(f'Player {self.name} total credits: {self.play_credits}')
        return self.play_credits

    def withdraw_credits(self, amount):
        '''withdraw credits'''
        if self.play_credits - amount >= 0:
            self.add_credits(amount)
            return True
        else:
            return False


class Dealer(Participant):
    '''Dealer specific actions'''
