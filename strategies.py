from move import my_move
from utils import best_player
from utils import random_player

import random

strategies = {}


def strategy_run(move: my_move, id: int, cnt: int, roll: int, state: list):

    move.move_me()
    return move


strategies["run"] = strategy_run


def strategy_drag_down(move: my_move, id: int, cnt: int, roll: int, state: list):

    if state[id] < 10:
        move.move_me()
        return move

    best_player_id, best_player_pos = best_player(cnt, state)

    # don't let them win!
    if best_player_id != id and best_player_pos > 23:
        move.move_other(best_player_id)
        return move

    if best_player_id != id and best_player_pos - state[id] < 6:
        move.move_other(best_player_id)
        return move

    move.move_me()
    return move


strategies["drag"] = strategy_drag_down


def strategy_second_until_end(move: my_move, id: int, cnt: int, roll: int, state: list):

    if state[id] < 10:
        move.move_me()
        return move

    best_player_id, best_player_pos = best_player(cnt, state)

    if best_player_id != id and best_player_pos > 27:
        move.move_other(best_player_id)
        return move

    # rush to the end
    if best_player_id == id and state[id] > 20:
        move.move_me()
        return move

    if best_player_id != id and best_player_pos > 20:
        move.move_me()
        return move

    # stay second
    if state[id] + roll < best_player_pos:
        move.move_me()
        return move

    other = random_player(cnt, [id, best_player_id])
    move.move_other(other)
    return move


strategies["second"] = strategy_second_until_end


def strategy_chaos(move: my_move, id: int, cnt: int, roll: int, state: list):

    walk = random.choice([True, True, False])
    if walk:
        move.move_me()
        return move

    other = random_player(cnt, [id])
    move.move_other(other)
    return move


strategies["chaos"] = strategy_chaos


def strategy_big_steps(move: my_move, id: int, cnt: int, roll: int, state: list):

    if roll > 3:
        move.move_me()
        return move

    best_player_id, _ = best_player(cnt, state)
    if best_player_id == id:
        move.move_me()
        return move

    move.move_other(best_player_id)
    return move


strategies["big"] = strategy_big_steps


def strategy_waiting(move: my_move, id: int, cnt: int, roll: int, state: list):

    if state[id] + roll <= 25:
        move.move_me()
        return move

    best_player_id, _ = best_player(cnt, state)

    if best_player_id != id:
        move.move_other(best_player_id)
        return move

    other = random_player(cnt, [id])
    move.move_other(other)
    return move


strategies["waiting"] = strategy_waiting
