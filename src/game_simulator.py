from src.game_state import GameState
import random
import sys
import copy
import time

SLEEP_TIME = 1

def simulate(players, observe=False, silent=False):
    num_players = len(players)
    deck = list(range(3, 36))
    random.shuffle(deck)

    gs = GameState(players)

    while deck:
        card = deck.pop()
        if observe:
            print(f'{card} is drawn')
            print(f'player tokens: {gs.player_tokens}')
            print(f'player cards: {gs.player_cards}')
            time.sleep(SLEEP_TIME)

        tokens = 0
        while True:
            p = players[gs.current_turn]
            if gs.player_tokens[p.name] == 0 or p.decideOnCard(card, tokens, copy.deepcopy(gs)):
                if observe:
                    print(f'{p.name} takes the card {card} with {tokens} tokens')
                    print('')
                    time.sleep(SLEEP_TIME)
                gs.player_tokens[p.name] += tokens
                gs.player_cards[p.name].append(card)
                gs.player_cards[p.name].sort()
                break
            else:
                tokens += 1
                gs.player_tokens[p.name] -= 1
                gs.current_turn = (gs.current_turn + 1) % num_players
                if observe:
                    print(f'{p.name} puts a token on the card {card}')
                    time.sleep(SLEEP_TIME)

    if not silent:
        print("GAME CONCLUDED. FINAL SCORE")
    winner_score = sys.maxsize
    winner_name = "No Winner"
    for p in players:
        score = gs.score(p.name)
        if not silent:
            print(f'{p.name}: {score}')
        if (score < winner_score):
            winner_name = p.name
            winner_score = score

    if not silent:
        print('')
        print('')
        print(f'Winner is: {winner_name}')

    for p in players:
        p.notify_game_end(winner_name, winner_score, gs)
    return winner_name



