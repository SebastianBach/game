import string
import unittest
from game.engine import game_engine
from game.move import my_move
from game.strategies import strategies
from ui.args import *
import random


def run_strategy(state: list, id: int, roll: int, test: string):
    move = my_move(len(state), roll, id)
    res = strategies[test](move, id, len(state), roll, state)
    return res.list()


class TestStrategyRun(unittest.TestCase):

    def test_base(self):
        res = run_strategy([0, 0, 0, 0], 0, 3, "run")
        self.assertEqual(res, [3, 0, 0, 0])


class TestStrategyBigSteps(unittest.TestCase):

    def test_big_value_4(self):
        res = run_strategy([0, 0, 0, 0], 0, 4, "big")
        self.assertEqual(res, [4, 0, 0, 0])

    def test_big_value_5(self):
        res = run_strategy([0, 0, 0, 0], 0, 5, "big")
        self.assertEqual(res, [5, 0, 0, 0])

    def test_big_value_6(self):
        res = run_strategy([0, 0, 0, 0], 0, 6, "big")
        self.assertEqual(res, [6, 0, 0, 0])

    def test_big_best_player(self):
        res = run_strategy([10, 9, 8, 7], 0, 1, "big")
        self.assertEqual(res, [1, 0, 0, 0])

    def test_big_move_other(self):
        res = run_strategy([7, 12, 8, 5], 0, 2, "big")
        self.assertEqual(res, [0, -2, 0, 0])


class TestStrategyWaiting(unittest.TestCase):

    def test_waiting_move(self):
        res = run_strategy([0, 0, 0, 0], 0, 5, "waiting")
        self.assertEqual(res, [5, 0, 0, 0])

        res = run_strategy([20, 0, 0, 0], 0, 5, "waiting")
        self.assertEqual(res, [5, 0, 0, 0])

    def test_waiting_move_best_player(self):

        res = run_strategy([22, 23, 20, 10], 0, 5, "waiting")
        self.assertEqual(res, [0, -5, 0, 0])

        random.seed(0)
        res = run_strategy([22, 20, 19, 10], 0, 5, "waiting")
        self.assertEqual(res, [0, 0, -5, 0])


class TestStrategyDrag(unittest.TestCase):

    def test_drag_move(self):
        res = run_strategy([9, 0, 0, 0], 0, 4, "drag")
        self.assertEqual(res, [4, 0, 0, 0])

    def test_drag_stop_winner(self):
        res = run_strategy([10, 24, 0, 0], 0, 4, "drag")
        self.assertEqual(res, [0, -4, 0, 0])

        res = run_strategy([10, 15, 0, 0], 0, 4, "drag")
        self.assertEqual(res, [0, -4, 0, 0])

    def test_drag_catch_up(self):
        res = run_strategy([10, 20, 0, 0], 0, 5, "drag")
        self.assertEqual(res, [5, 0, 0, 0])

    def test_drag_winning(self):
        res = run_strategy([20, 18, 15, 7], 0, 5, "drag")
        self.assertEqual(res, [5, 0, 0, 0])


class TestStrategySecond(unittest.TestCase):

    def test_second_move(self):
        res = run_strategy([9, 0, 0, 0], 0, 5, "second")
        self.assertEqual(res, [5, 0, 0, 0])

    def test_second_stop_best(self):
        res = run_strategy([15, 28, 0, 0], 0, 5, "second")
        self.assertEqual(res, [0, -5, 0, 0])

        res = run_strategy([18, 25, 0, 0], 0, 5, "second")
        self.assertEqual(res, [5, 0, 0, 0])

    def test_second_winning(self):
        res = run_strategy([21, 20, 0, 0], 0, 5, "second")
        self.assertEqual(res, [5, 0, 0, 0])

    def test_second_stay_second(self):
        res = run_strategy([15, 18, 0, 0], 0, 2, "second")
        self.assertEqual(res, [2, 0, 0, 0])

        random.seed(0)
        res = run_strategy([15, 18, 0, 0], 0, 4, "second")
        self.assertEqual(res, [0, 0, 0, -4])


class BasicEngineTests(unittest.TestCase):

    def test_base(self):
        players = ["run", "run", "run"]
        res = game_engine(players, 123, 0.0)
        self.assertEqual(res, [27, 30, 18])

        players = ["chaos", "chaos", "chaos"]
        res = game_engine(players, 123, 0.0)
        self.assertEqual(res, [32, 19, 11])


class ArgsParsterTests(unittest.TestCase):

    def test_args_ok(self):

        args = ["app.exe", "show", "123", "run", "run"]
        res = args_ok(args, strategies)
        self.assertTrue(res)

    def test_args_bad_cnt(self):

        args = ["app.exe", "show", "123", "run"]
        res = args_ok(args, strategies)
        self.assertFalse(res)

    def test_args_bad_mode(self):

        args = ["app.exe", "something", "123", "run", "run"]
        res = args_ok(args, strategies)
        self.assertFalse(res)

    def test_args_bad_seed(self):

        args = ["app.exe", "show", "seed", "run", "run"]
        res = args_ok(args, strategies)
        self.assertFalse(res)

    def test_args_bad_player(self):

        args = ["app.exe", "show", "123", "run", "_BAD_"]
        res = args_ok(args, strategies)
        self.assertFalse(res)

    def test_args_parse(self):

        args = ["app.exe", "show", "123", "run", "big"]
        seed, players, delay = parse_args(args)
        self.assertEqual(seed,123)
        self.assertEqual(players,["run", "big"])
        self.assertEqual(delay,0.7)

if __name__ == '__main__':
    unittest.main()
