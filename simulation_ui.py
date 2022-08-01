from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout
from PySide6.QtCore import QTimer
from PySide6 import QtWidgets
import sys

from ui.args import *
from game.engine import GameEngine
from game.strategies import strategies
from ui.draw import draw


class GameState:
    def set(self, player_id, roll, res, state, history, players):
        self.player_id = player_id
        self.roll = roll
        self.res = res
        self.state = state
        self.history = history
        self.players = players


class GameData:
    def __init__(self, seed: int, players: list):
        self.game = GameEngine(seed, players)
        self.players = players
        self.end = False
        self.history = []
        for i in range(len(players)):
            self.history.append([])

    def next(self):
        game_end, player_id, _, roll, _, res, state = self.game.next_player()

        self.player_id = player_id
        self.roll = roll
        self.res = res
        self.state = state

        indx = 0
        for pos in state:
            if pos != 0:
                self.history[indx].append(pos)
            indx = indx + 1

        if game_end:
            self.end = True

    def get_state(self):

        game_state = GameState()
        game_state.set(self.player_id, self.roll, self.res,
                       self.state, self.history, self.players)
        return game_state

    def has_ended(self):
        return self.end


class GameWidget(QtWidgets.QWidget):

    def __init__(self, width):
        super(GameWidget, self).__init__()
        self.state = None

        self.setMinimumSize(width, 620)

    def set_state(self, game_state):

        self.state = game_state

    def paintEvent(self, e):

        if self.state is not None:
            draw(self.width(), 620, self.state.player_id, self.state.roll, self.state.res,
                 self.state.state, self.state.history, self.state.players, self)


class ApplicatioWindow(QDialog):

    def __init__(self, seed: int, players: list, delay: float, parent=None):
        super(ApplicatioWindow, self).__init__(parent)

        self.setWindowTitle("Game Simulation")

        width = len(players) * 80

        self.wid = GameWidget(width)
        layout = QVBoxLayout(self)
        layout.addWidget(self.wid)

        self.setStyleSheet("background-color: black;")

        self.game = GameData(seed, players)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.next)
        self.timer.start(delay * 1000)

    def next(self):

        if self.game.has_ended():
            return

        self.game.next()
        state = self.game.get_state()

        if self.game.has_ended():
            print("end of game")
            print("Winner is player {}".format(state.player_id+1))
            self.timer.stop()

        self.wid.set_state(state)
        self.wid.repaint()


if __name__ == "__main__":

    # command line arguments

    if not args_ok(sys.argv, strategies):
        print("insufficient or invalid command line args")
        exit()

    seed, players, delay = parse_args(sys.argv)

    app = QApplication(sys.argv)
    form = ApplicatioWindow(seed, players, delay)

    form.show()
    app.exec_()
