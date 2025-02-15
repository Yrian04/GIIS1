import config
from ..utils.sign import sign
from .abc.line_drawer import LineDrawer



class LineBresenhamDrawer(LineDrawer):
    def __init__(self, start, end, color = config.standart_color):
        super().__init__(start, end, color)

        self._next = list(start)
        self._delta = self.end[0] - self.start[0], self.end[1] - self.start[1]
        self._error = self._delta[1] * 2 - self._delta[0]
        self._counter = 0
        self._main_axis = 0 if abs(self._delta[0]) > abs(self._delta[1]) else 1
        self._sub_axis = abs(self._main_axis - 1)

    def draw(self, canvas):
        if self._counter > abs(self._delta[self._main_axis]):
            return False
        
        canvas.set(*self._next, self.color)

        if self._error >= 0:
            self._next[self._sub_axis] += sign(self._delta[self._sub_axis])
            self._error -= 2 * abs(self._delta[self._main_axis])

        self._next[self._main_axis] += sign(self._delta[self._main_axis])
        self._error += 2 * abs(self._delta[self._sub_axis])
        self._counter += 1
        
        return True
