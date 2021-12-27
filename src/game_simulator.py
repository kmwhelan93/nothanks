from src.game_state import GameState
import random
import sys
import copy

def simulate(players, silent=False):
    num_players = len(players)
    deck = list(range(3, 36))
    random.shuffle(deck)

    gs = GameState(num_players)

    while deck:
        card = deck.pop()
        tokens = 0
        while True:
            p = players[gs.current_turn]
            if gs.player_tokens[gs.current_turn] == 0 or p.decideOnCard(card, tokens, copy.deepcopy(gs)):
                gs.player_tokens[gs.current_turn] += tokens
                gs.player_cards[gs.current_turn].append(card)
                break
            else:
                tokens += 1
                gs.player_tokens[gs.current_turn] -= 1
                gs.current_turn = (gs.current_turn + 1) % num_players


    print("GAME CONCLUDED. FINAL SCORE")
    winner_score = sys.maxsize
    winner_index = -1
    for i in range(num_players):
        score = gs.score(i)
        print(f'{players[i].name}: {score}')
        if (score < winner_score):
            winner_index = i
            winner_score = score

    print('')
    print('')
    print(f'Winner is: {players[winner_index].name}')
    return winner_index



