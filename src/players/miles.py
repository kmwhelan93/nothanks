
class Miles:
    def __init__(self):
        self.name = "Miles bot"

    def decideOnCard(self, card, tokens, game_state):
        my_cards = game_state.player_cards[game_state.current_turn]
        my_tokens = game_state.player_tokens[game_state.current_turn]
        if card < 10:
            return True
        if card - tokens < 11:
            return True
        if self.one_off(card, my_cards):
            return True
        return False

    # 6
    # [7, 8]

    def one_off(self, card, my_cards):
        for x in my_cards:
            if x - card == 1:
                return True
        return False

