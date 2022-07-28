import random
from random import randint
from move import my_move
from strategies import strategies
from operator import add
from time import sleep


def game_engine(players: list, seed: int, delay: float):

    player_cnt = len(players)
    state = [0] * player_cnt

    # run simulation

    random.seed(seed)

    for r in range(20):
        for p in range(player_cnt):

            roll = randint(1, 6)
            move = my_move(player_cnt, roll, p)

            my_strategy = players[p]

            # just win
            if state[p] + roll >= 30:
                move.move_me()
            else:
                # act according to strategy
                move = strategies[my_strategy](
                    move, p, player_cnt, roll, state)

            res = move.list()

            state = list(map(add, state, res))

            for i in range(player_cnt):
                if state[i] < 0:
                    state[i] = 0

            print("Player {} ({}) rolled {}, action is {}!".format(
                p+1, my_strategy, roll, res))
            print(state)

            for i in range(player_cnt):
                if state[i] >= 30:
                    print("Player {} won!".format(p+1))
                    return state
            if delay > 0.0:
                sleep(delay)

    return state
