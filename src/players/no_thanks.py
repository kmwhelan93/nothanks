
class NoThanksPlayer:
    def __init__(self, name):
        self.name = name

    def decideOnCard(self, card, tokens, game_state):
        return False
