from src import game_simulator
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
    print("------------------")
    print("AGGREGATE RESULTS:")
    for name, w in wins.items():
        print(f'{name} won {w}')
    winner = max(wins, key=wins.get)
    print('')
    print(f'Overall winner is: {winner}, winning {round(wins[winner] / num_games * 100)}% of games')


if __name__ == "__main__":
    num_games = 100
    players = [RandomPlayer("Random Joe"), RandomPlayer("Random Paul"), RandomPlayer("Random Sam")]
    simulate_games(players, num_games)