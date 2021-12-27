from collections import defaultdict

class GameState:
    def __init__(self, num_players):
        self.current_turn = 0
        self.player_cards = {key: [] for key in range(num_players)}
        initial_token_count = 11 if num_players < 6 else 9
        self.player_tokens = {key: initial_token_count for key in range(num_players)}

    def score(self, index):
        cards = self.player_cards[index]
        cards.sort()
        counted_cards = []
        for i in range(len(cards)):
            if i == 0 or cards[i] - cards[i-1] > 1:
                counted_cards.append(cards[i])
        return sum(counted_cards) - self.player_tokens[index]
