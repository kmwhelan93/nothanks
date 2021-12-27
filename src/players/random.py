import random

class RandomPlayer:
    def __init__(self, name):
        self.name = name

    def decideOnCard(self, card, tokens, game_state):
        if random.random() > .5:
            return True
        else:
            return False
