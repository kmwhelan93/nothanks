
class Miles:
    def __init__(self):
        self.name = "Miles bot"

    def decideOnCard(self, card, tokens, game_state):
        my_cards = game_state.player_cards[self.name]
        my_tokens = game_state.player_tokens[self.name]
        opp_cards = self.opponent_cards(card, game_state)
        opp_distance = self.calculate_min_distance(card, opp_cards)
        my_distance = self.calculate_min_distance(card, my_cards)
        opponent_low_on_tokens = self.opponent_low_on_tokens(game_state)
        if card < 10:
            return True
        if card - tokens < 11:
            return True
        if card - 2 * tokens < 10:
            return True
        if tokens > 10:
            return True
        if my_distance == 1:
            if opp_distance < 2 or 5 < tokens or opponent_low_on_tokens:
                return True
            else:
                return False
        # if my_distance == 2:
        #     if opp_distance < 2 or 5 < tokens or opponent_low_on_tokens:
        #         return True
        #     else:
        #         return False
        return False

    def opponent_low_on_tokens(self, game_state):
        for player, tokens in game_state.player_tokens.items():
            if player != self.name and tokens < 2:
                return True
        return False

    def calculate_min_distance(self, card, cards):
        min_distance = 45
        for c in cards:
            distance = abs(card - c)
            if distance < min_distance:
                min_distance = distance
        return min_distance


    def opponent_cards(self, card, game_state):
        oppo_cards = []
        for player, cards in game_state.player_cards.items():
            if player != self.name:
                oppo_cards = oppo_cards + cards
        return oppo_cards

    def notify_game_end(self, winner_name, winner_score, game_state):
        pass
