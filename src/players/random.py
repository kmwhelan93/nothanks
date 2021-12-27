import random

class RandomPlayer:
    def decideOnCard(self, card, gameState):
        if random.random() > .5:
            return True
        else:
            return False
