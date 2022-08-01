import sys

modes = {}
modes["show"] = 0.7
modes["run"] = 0.02


def args_ok(args, strategies):
    # at least two players
    if len(args) < 5:
        return False

    if args[1] not in modes:
        return False

    if not args[2].isdigit():
        return False

    for player in args[3:]:
        if not player in strategies:
            return False

    return True


def parse_args(args):
    mode = args[1]
    delay = modes[mode]

    seed = int(args[2])
    players = args[3:]

    return seed, players, delay
