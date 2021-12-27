from src.GameState import GameState
from src.players.random import RandomPlayer
import random
import sys
import copy

NUM_PLAYERS = 3

if __name__ == "__main__":
    players = [RandomPlayer() for element in range(NUM_PLAYERS)]
    deck = list(range(3, 36))
    random.shuffle(deck)

    gs = GameState(NUM_PLAYERS)

    while deck:
        card = deck.pop()
        tokens = 0
        while True:
            p = players[gs.current_turn]
            if gs.player_tokens[gs.current_turn] == 0 or p.decideOnCard(card, copy.deepcopy(gs)):
                gs.player_tokens[gs.current_turn] += tokens
                gs.player_cards[gs.current_turn].append(card)
                break
            else:
                tokens += 1
                gs.player_tokens[gs.current_turn] -= 1
                gs.current_turn = (gs.current_turn + 1) % NUM_PLAYERS


    print("GAME CONCLUDED. FINAL SCORE")
    winner_score = sys.maxsize
    winner_index = -1
    for i in range(NUM_PLAYERS):
        score = gs.score(i)
        print(f'Player {i}: {score}')
        if (score < winner_score):
            winner_index = i
            winner_score = score

    print('')
    print('')
    print(f'Winner is: {winner_index}')



