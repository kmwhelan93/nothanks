import random

class RandomPlayer:
    def __init__(self, name):
        self.name = name

    def decideOnCard(self, card, tokens, gameState):
        if random.random() > .5:
            return True
        else:
            return False
