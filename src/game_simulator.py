from src.game_state import GameState
import random
import sys
import copy
import time

SLEEP_TIME = 2

def simulate(players, observe=False):
    num_players = len(players)
    deck = list(range(3, 36))
    random.shuffle(deck)

    gs = GameState(num_players)

    while deck:
        card = deck.pop()
        if observe:
            print(f'{card} is drawn')
            formatted_tokens = {players[key].name: gs.player_tokens[key] for key in range(num_players)}
            formatted_cards = {players[key].name: gs.player_cards[key] for key in range(num_players)}
            print(f'player tokens: {formatted_tokens}')
            print(f'player cards: {formatted_cards}')
            time.sleep(SLEEP_TIME)

        tokens = 0
        while True:
            p = players[gs.current_turn]
            if gs.player_tokens[gs.current_turn] == 0 or p.decideOnCard(card, tokens, copy.deepcopy(gs)):
                if observe:
                    print(f'{p.name} takes the card {card}')
                    print('')
                    time.sleep(SLEEP_TIME)
                gs.player_tokens[gs.current_turn] += tokens
                gs.player_cards[gs.current_turn].append(card)
                break
            else:
                tokens += 1
                gs.player_tokens[gs.current_turn] -= 1
                gs.current_turn = (gs.current_turn + 1) % num_players
                if observe:
                    print(f'{p.name} puts a token on the card {card}')
                    time.sleep(SLEEP_TIME)


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



