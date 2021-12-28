
class HumanPlayer:
    def __init__(self, name):
        self.name = name

    def decideOnCard(self, card, tokens, game_state):
        decision = "na"
        while not ["y", "n"].__contains__(decision):
            print(f'Tokens: {game_state.player_tokens}')
            decision = input(f'Will you take {card} with {tokens} tokens? (y/n): ')
        return decision == "y"

    def notify_game_end(self, winner_name, winner_score, game_state):
        pass

