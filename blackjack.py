'''contains the blackjack class'''


class Blackjack:
    '''handles the blackjack specific rules'''

    def __init__(self, deck, dealer, *args):
        self.deck = deck
        self.dealer = dealer
        self.players = list(args)
        self.start_game(self.deck, self.dealer, self.players)

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


    def start_game(self, deck, dealer, players):
        '''runs a round of blackjack'''
        active_players = self.check_credits(players)
        bets = self.player_bets(active_players)

        # print('Bets placed')
        # print('The dealers face card is...')
        # print(dealer.cards[0][1], dealer.cards[0][0])
        # scores = {}
        # for index, player in enumerate(self.players):
        #     print(f'Player {index}s cards are')
        #     for card in player.cards:
        #         print(card[1], card[0])
        #     scores[f'Player{index}'] = self.calculate_score(player.cards)
        # if 21 in scores.values():
        #     blackjack_string = 'Blackjack for '
        #     for player, score in scores.items():
        #         if score == 21:
        #             blackjack_string += player
        #             print('removing', player[-1])
        #             completed_players.append(players.pop(int(player[-1])))

        #     blackjack_string += '!!'
        #     print(blackjack_string)

        #     if self.calculate_score(self.dealer.cards) == 21:
        #         print('Dealer natural')

        # for player in players:
        #     hit_stand = input('Hit? (y/n)')
        #     if hit_stand == 'y':
        #         player.get_card(deck)
        #     else:
        #         completed_players.append(print('standing'))
