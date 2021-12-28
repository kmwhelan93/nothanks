import random

SAFE_TOKENS = 7

class KevinBot:
    def __init__(self):
        self.name = "Kevin bot"
        self.aggression = -8
        self.relative_aggressions = {'Miles bot': 5, 'Liam': -50, 'NoThanks Ninny': -100, 'Liam Human': 0}

        self.aggression_wins = 0
        self.relative_aggression_wins = {'Miles bot': 0, 'Liam': 0, 'NoThanks Ninny': 0, 'Liam Human': 0}

    def decideOnCard(self, card, tokens, game_state):
        my_cards = game_state.player_cards[self.name]
        my_tokens = game_state.player_tokens[self.name]
        opp_cards = self.opp_cards(game_state, self.name)
        all_cards = self.all_cards(game_state)
        opp_tokens = self.opp_tokens(game_state)
        min_opp_tokens = min(opp_tokens)
        opp_distance = self.min_distance(card, opp_cards)
        my_distance = self.min_distance(card, my_cards)
        my_card_value = self.card_value(self.name, card, tokens, game_state)
        (max_opp_card_value, max_opp_value_player) = self.max_opp_card_value(card, tokens, game_state)

        if len(my_cards) == 2 and len(all_cards) == 2:
            return False
        return my_card_value > -1 * self.aggression \
               or (max_opp_card_value > 0 and my_card_value > 1)

    def max_opp_card_value(self, card, tokens, game_state):
        max = -100
        max_p = ''
        for p in game_state.player_cards.keys():
            if p != self.name:
                v = self.card_value(p, card, tokens, game_state) + self.relative_aggressions[p]
                if v > max:
                    max = v
                    max_p = p
        return (max, max_p)

    def card_value(self, player, card, tokens, game_state):
        player_cards = game_state.player_cards[player]
        opp_cards = self.opp_cards(game_state, player)
        opp_distance = self.min_distance(card, opp_cards)
        if opp_distance == 100:
            opp_distance = 3
        player_tokens = game_state.player_tokens[player]
        card_distance = self.min_distance(card, player_cards)
        if card_distance == 100:
            card_distance = 3
        could_connect = self.could_connect_card(card, player_cards, opp_cards)
        low_token_value = max(7 - player_tokens, 0)

        leverage = abs(opp_distance)*2

        values = [2*tokens, low_token_value, leverage]

        if player_tokens == 0:
            values.append(500)

        if card_distance == -1:
            values.append(1)
        elif card_distance == 1:
            values.append(0)
        elif not could_connect:
            values.append(-1*card)
        else:
            values.append(-1 * card / 2 - card_distance / 5)
        # if player == self.name:
        #     print(f'values: {values}, sum: {sum(values)}')
        return sum(values)

    def could_connect_card(self, card, cards, opp_cards):
        if len(opp_cards) == 0 or card < min(opp_cards) or card > max(opp_cards):
            return True
        for my_card in cards:
            for c in range(my_card, card, 1 if card > my_card else -1):
                if c in opp_cards:
                    continue
            return True
        return False


    def min_distance(self, card, locations):
        min = 100
        for c in locations:
            if abs(c - card) < abs(min):
                min = card - c
        return min

    def opp_cards(self, game_state, player):
        return [card for name, cards in game_state.player_cards.items() if player != name for card in cards]

    def all_cards(self, game_state):
        return [card for name, cards in game_state.player_cards.items() for card in cards]

    def opp_tokens(self, game_state):
        return [token for name, token in game_state.player_tokens.items() if name != self.name]

    def notify_game_end(self, winner_name, winner_score, game_state):
        if winner_name != self.name:
            my_cards = game_state.player_cards[self.name]
            winner_cards = game_state.player_cards[winner_name]
        #     if len(my_cards) < len(winner_cards) and my_cards < 25:
        #         if self.aggression_wins < self.relative_aggression_wins[winner_name] / 3:
        #             self.aggression += random.random()
        #             self.relative_aggressions[winner_name] += random.random() / 10
        #         else:
        #             self.aggression += random.random() / 10
        #             self.relative_aggressions[winner_name] += random.random()
        #     else:
        #         if self.aggression_wins < self.relative_aggression_wins[winner_name] / 3:
        #             self.aggression -= random.random()
        #             self.relative_aggressions[winner_name] -= random.random() / 10
        #         else:
        #             self.aggression -= random.random() / 10
        #             self.relative_aggressions[winner_name] -= random.random()
        # print(f'agg: {self.aggression}, relagg: {self.relative_aggressions}')
        self.aggression_wins = 0
        self.relative_aggression_wins = {'Miles bot': 0, 'Liam': 0, 'NoThanks Ninny': 0}
