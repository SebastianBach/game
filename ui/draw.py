from PySide6 import QtGui
from PySide6 import QtCore


def pos_to_screen(pos: int):
    return 550 - (pos * 15)


def draw_lines(painter, width):
    # draw lines

    pen = QtGui.QPen(QtGui.QColor(30, 30, 30), 1,   QtCore.Qt.SolidLine)
    painter.setPen(pen)

    for i in range(30):
        offset = pos_to_screen(i)
        painter.drawLine(0, offset, width, offset)

    pen = QtGui.QPen(QtGui.QColor(55, 55, 55), 3,   QtCore.Qt.SolidLine)
    painter.setPen(pen)

    base = pos_to_screen(0)
    painter.drawLine(0, base, width, base)

    top = pos_to_screen(30)
    painter.drawLine(0, top, width, top)

    line24 = pos_to_screen(24)
    painter.drawLine(0, line24, width, line24)


def draw_history(painter, history, indx, pos_x):
    # paint history

    pen = QtGui.QPen(QtGui.QColor(100, 100, 100),
                     1,   QtCore.Qt.SolidLine)
    painter.setPen(pen)

    for pos in history[indx]:
        h = pos_to_screen(pos)
        painter.drawLine(pos_x-3, h, pos_x+3, h)
        painter.drawLine(pos_x, h+1, pos_x, h-1)


dir_to_style = {}
dir_to_style[True] = QtGui.QPen(
    QtGui.QColor(0, 255, 0), 2,   QtCore.Qt.SolidLine)
dir_to_style[False] = QtGui.QPen(
    QtGui.QColor(255, 0, 0), 2,   QtCore.Qt.SolidLine)


def draw_movement(painter, res, indx, pos_x, pos_y):
    if res[indx] != 0:
        painter.setPen(dir_to_style[res[indx] > 0])
        painter.drawLine(pos_x, pos_y, pos_x, pos_y + res[indx] * 15)


player_to_color = {}
player_to_color[True] = QtGui.QColor(220, 220, 220)
player_to_color[False] = QtGui.QColor(150, 150, 150)


def draw_player(painter, indx, player_id, pos_x, pos_y, roll, players):

    color = player_to_color[indx == player_id]

    # pawn
    brush = QtGui.QBrush()
    brush.setStyle(QtCore.Qt.SolidPattern)
    brush.setColor(color)
    painter.setBrush(brush)

    painter.setPen(QtGui.Qt.NoPen)
    painter.drawEllipse(pos_x-5, pos_y-5, 10, 10)

    # strategy
    pen = QtGui.QPen(color,
                     1,   QtCore.Qt.SolidLine)
    painter.setPen(pen)
    small_font = QtGui.QFont()
    small_font.setPixelSize(12)
    painter.setFont(small_font)
    painter.drawText(pos_x+15, pos_y+5, players[indx])


def draw_players(painter, state, history, res, player_id, roll, players):
    indx = 0
    player_x = 10
    for pos in state:

        # movement
        pos_x = player_x
        pos_y = pos_to_screen(pos)

        draw_history(painter, history, indx, pos_x)

        draw_movement(painter, res, indx, pos_x, pos_y)

        draw_player(painter, indx, player_id, pos_x, pos_y, roll, players)

        player_x = player_x + 80
        indx = indx + 1


roll_to_icon = {}
roll_to_icon[1] = "\u2680"
roll_to_icon[2] = "\u2681"
roll_to_icon[3] = "\u2682"
roll_to_icon[4] = "\u2683"
roll_to_icon[5] = "\u2684"
roll_to_icon[6] = "\u2685"


def draw_roll(painter, roll, player_id):

    pos_x = player_id * 80

    pen = QtGui.QPen(QtGui.QColor(220, 220, 220),
                     1,   QtCore.Qt.SolidLine)
    painter.setPen(pen)

    font = QtGui.QFont()
    font.setPixelSize(50)

    # roll
    painter.setFont(font)
    painter.drawText(pos_x, 70, roll_to_icon[roll])


def draw(width, height, player_id, roll, res, state, history, players, parent):

    painter = QtGui.QPainter()
    painter.begin(parent)

    draw_lines(painter, width)

    draw_players(painter, state, history, res, player_id, roll, players)

    draw_roll(painter, roll, player_id)

    painter.end()
