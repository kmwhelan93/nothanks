from src import game_simulator
from src.players.miles import Miles
from src.players.no_thanks import NoThanksPlayer
from src.players.random import RandomPlayer
import random

def simulate_games(players, num_games):
    wins = {players[key].name: 0 for key in range(len(players))}
    for i in range(num_games):
        random.shuffle(players)
        winner = game_simulator.simulate(players)
        wins[players[winner].name] += 1

    print("------------------")
    print("------------------")
    print("AGGREGATE RESULTS:")
    for name, w in wins.items():
        print(f'{name} won {w}')
    winner = max(wins, key=wins.get)
    print('')
    print('=====================')
    print(f'Overall winner is: {winner}, winning {round(wins[winner] / num_games * 100)}% of games')
    print('=====================')

def observe_game(players):
    game_simulator.simulate(players, observe=True)

if __name__ == "__main__":
    num_games = 1000
    players = [NoThanksPlayer("NoThanks Ninny"), Miles(), RandomPlayer("Random Ronald")]
    simulate_games(players, num_games)
    observe_game(players)