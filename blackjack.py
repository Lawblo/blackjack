'''contains the blackjack class'''


class Blackjack:
    '''handles the blackjack specific rules'''

    def __init__(self, deck, dealer, *args):
        self.deck = deck
        self.dealer = dealer
        self.players = list(args)
        self.results = {
            'blackjack': [],
            'win': [],
            'draw': [],
            'loss': [],
        }
        self.start_game()
        self.payout()

    def add_player(self, player):
        '''adds a player'''
        self.players.append(player)

    def remove_player(self, player):
        '''removes a player'''
        self.players.remove(player)

    def calculate_score(self, hand: list) -> int:
        '''
        get the value of the hand
        hand:
        '''
        total = 0
        for card in hand:
            total += card[2]
        for card in hand:
            if total > 21 and 'A' in card:
                total -= 10
        return total

    def check_credits(self, players):
        '''removes players with no credits'''
        has_credits = []
        for player in players:
            if player.get_credits():
                has_credits.append(player)
            else:
                print(f'Player {player.name} has no credits')
                print(f'Player {player.name} removed from play')
                print('Add credits to join the next game')
        return has_credits

    def player_bets(self, players):
        '''get playerbet'''
        bets = {}
        for player in players:
            print(f'\nPlayer {player.name}, place your bet!')
            print('Credits available:', f'{player.get_credits():>12}')
            while True:
                bet = self.enter_bet()
                if player.withdraw_credits(bet):
                    bets[player.name] = bet
                    break
                else:
                    print('Not enough credits in account')
        print('\nALL BETS PLACED\n')
        return bets

    def enter_bet(self):
        '''validate bet input'''
        while True:
            try:
                bet = int(input('Bet: '))
            except ValueError:
                print('Wrong input')
                continue
            else:
                return bet

    def display_playercards(self, player):
        '''shows the players hand'''
        print(f'{player.name.capitalize()}s cards are')
        for card in player.cards:
            print(card[1], card[0])

    def payout(self):
        pass

    def start_game(self):
        '''runs a round of blackjack'''
        active_players = self.check_credits(self.players)


        bets = self.player_bets(active_players)

        print('The dealers face card is...')
        print(self.dealer.cards[0][1], self.dealer.cards[0][0])

        for player in active_players:
            self.display_playercards(player)

        scores = {player.name: self.calculate_score(player.cards) \
                  for player in active_players}

        if 21 in scores.values():
            if self.calculate_score(self.dealer.cards) == 21:
                self.results['draw'].extend([player for player in active_players if self.calculate_score(player.cards) == 21])
                self.results['loss'].extend([player for player in active_players if player not in self.results['draw']])
            else:
                pass
                # PAYOUT
