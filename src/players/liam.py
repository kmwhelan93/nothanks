
class LiamBot:
    def __init__(self):
        self.name = "Liam"

    def decideOnCard(self, card, tokens, game_state):
        my_cards = game_state.player_cards[self.name]
        my_tokens = game_state.player_tokens[self.name]
        other_cards = self.get_other_cards(game_state)
        if card <= 8:
            return True
        elif tokens > 8:
            return True
        elif card > 8:
            for cards in my_cards:
                if cards +- 2 == card or cards +- 1 == card:
                    for other_card in other_cards:
                        if other_card +- 1 == card:
                            return False
                        else:
                            if tokens >= 8:
                                return True
                            else:
                                return False

    def get_other_cards(self, game_state):
        other_cards = []
        for player, cards in game_state.player_cards.items():
            if player != self.name:
                other_cards = other_cards + cards
        return other_cards

