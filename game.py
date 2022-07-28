import sys
from engine import game_engine

modes = {}
modes["show"] = 0.5
modes["run"] = 0.0

if __name__ == "__main__":

    # command line arguments

    if len(sys.argv[1:]) < 5:
        print("insufficient command line args")
        exit()

    mode = sys.argv[1]
    delay = modes[mode]

    seed = int(sys.argv[2])
    players = sys.argv[3:]

    game_engine(players, seed, delay)
