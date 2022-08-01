import random


def best_player(cnt: int, state: list):
    best_player_id = -1
    best_player_pos = -1
    for i in range(cnt):
        if state[i] > best_player_pos:
            best_player_pos = state[i]
            best_player_id = i

    return best_player_id, best_player_pos


def random_player(cnt: int, exclude: list):
    players = []
    for i in range(cnt):
        if i not in exclude:
            players.append(i)

    return random.choice(players)
