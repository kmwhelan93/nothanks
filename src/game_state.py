from collections import defaultdict

class GameState:
    def __init__(self, players):
        num_players = len(players)
        self.player_order = [p.name for p in players]
        self.current_turn = 0
        self.player_cards = {players[key].name: [] for key in range(num_players)}
        initial_token_count = 11 if num_players < 6 else 9
        self.player_tokens = {players[key].name: initial_token_count for key in range(num_players)}

    def score(self, name):
        cards = self.player_cards[name]
        cards.sort()
        counted_cards = []
        for i in range(len(cards)):
            if i == 0 or cards[i] - cards[i-1] > 1:
                counted_cards.append(cards[i])
        return sum(counted_cards) - self.player_tokens[name]
