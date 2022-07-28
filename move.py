
class my_move:
    def __init__(self, cnt: int, roll: int, id: int):
        self.res = [0] * cnt
        self.roll = roll
        self.id = id

    def move_me(self):
        self.res[self.id] = self.roll

    def move_other(self, id: int):
        self.res[id] = - self.roll

    def list(self):
        return self.res
