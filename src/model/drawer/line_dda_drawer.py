from ...utils.sign import sign
from ..abc.line_drawer import LineDrawer



class LineDDADrawer(LineDrawer):
    def __init__(self, start, end, color):
        super().__init__(start, end, color)
        self._i = 0
        self._delta = self.end[0] - self.start[0], self.end[1] - self.start[1]
        self._length = max(abs(self._delta[0]), abs(self._delta[1]))
        self._d = (self._delta[0] / self._length, self._delta[1] / self._length)
        self._next = self.start[0] + 0.5 * sign(self._d[0]), self.start[1] + 0.5 * sign(self._d[1])

    def draw(self, canvas) -> bool:
        if self._i > self._length:
            return False
        canvas.set(int(self._next[0]), int(self._next[1]), self.color)
        self._next = self._next[0] + self._d[0], self._next[1] + self._d[1]
        self._i += 1
        return True
