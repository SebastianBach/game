import random
from random import randint
from game.move import my_move
from game.strategies import strategies
from operator import add
from time import sleep


class GameEngine:
    def __init__(self, seed: int, players: list):
        random.seed(seed)
        self.player_cnt = len(players)
        self.players = players
        self.state = [0] * self.player_cnt
        self.id = id
        self.player = 0

    def check_end(self):
        for i in range(self.player_cnt):
            if self.state[i] >= 30:
                return True
        return False

    def next_player(self):

        roll = randint(1, 6)

        player_id = self.player
        initial_state = self.state

        move = my_move(self.player_cnt, roll, player_id)

        my_strategy = self.players[player_id]

        # just win
        if self.state[player_id] + roll >= 30:
            move.move_me()
        else:
            # act according to strategy
            move = strategies[my_strategy](
                move, player_id, self.player_cnt, roll, self.state)

        res = move.list()

        self.state = list(map(add, self.state, res))

        for i in range(self.player_cnt):
            if self.state[i] < 0:
                self.state[i] = 0

        self.player = player_id + 1
        if self.player >= self.player_cnt:
            self.player = 0

        game_end = self.check_end()

        return game_end, player_id, my_strategy, roll, initial_state, res, self.state


def game_engine(players: list, seed: int, delay: float):

    new_game = GameEngine(seed, players)

    for r in range(20 * len(players)):

        game_end, player_id, my_strategy, roll, initial_state, res, state = new_game.next_player()

        print("{} Player {} ({}) rolled {}, move is {}!".format(initial_state,
                                                                player_id+1, my_strategy, roll, res))

        if game_end:
            print("{} Player {} ({}) won!".format(
                state, player_id+1, my_strategy))
            return state

        if delay > 0.0:
            sleep(delay)


