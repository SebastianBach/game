import sys
from game.engine import game_engine
from ui.args import *
from game.strategies import strategies

if __name__ == "__main__":

    if not args_ok(sys.argv, strategies):
        print("insufficient or invalid command line args")
        exit()

    seed, players, delay = parse_args(sys.argv)

    game_engine(players, seed, delay)
