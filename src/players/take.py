
class TakePlayer:
    def __init__(self, name):
        self.name = name

    def decideOnCard(self, card, tokens, game_state):
        return True

    def notify_game_end(self, winner_name, winner_score, game_state):
        pass