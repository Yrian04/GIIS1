import config
from ..utils.sign import sign
from .abc.line_drawer import LineDrawer



class LineWuDrawer(LineDrawer):
    def __init__(self, start, end, color = config.standart_color):
        super().__init__(start, end, color)

        self._delta = self.end[0] - self.start[0], self.end[1] - self.start[1]
        self._main_axis = 0 if abs(self._delta[0]) > abs(self._delta[1]) else 1
        self._sub_axis = abs(self._main_axis - 1)
        if self._delta[self._main_axis] < 0:
            self.start, self.end = self.end, self.start
            self._delta = -self._delta[0], -self._delta[1]  
        self._error = 0
        self._counter = 0
        self._next = list(self.start)

    def draw(self, canvas):
        if self._counter > self._delta[self._main_axis]:
            return False

        if self._delta[0] == self._delta[1] or self._delta[0] == 0 or self._delta[1] == 0:
            canvas.set(
                self._next[0], 
                self._next[1], 
                self.color
            ) 
            self._next[0] += sign(self._delta[0])
            self._next[1] += sign(self._delta[1])
            self._counter += 1
            return True
        
        if self._counter == 0:
            canvas.set(
                self._next[0], 
                self._next[1], 
                self.color
            )
            self._counter += 1
            return True


        if abs(self._error) >= self._delta[self._main_axis]:
            self._next[self._sub_axis] += sign(self._delta[self._sub_axis])
            self._error -= 2 * self._delta[self._main_axis] * sign(self._delta[self._sub_axis])

        self._next[self._main_axis] += 1
        self._error += 2 * self._delta[self._sub_axis]
        self._counter += 1
        
        denominator = 2*self._delta[self._main_axis]
        numerator = self._error % denominator
        remainder1 = 1 if numerator > self._delta[self._main_axis] else 0
        remainder2 = 1 if numerator < self._delta[self._main_axis] else 0
        s1 = (self.color.s * (denominator - numerator)) // denominator + remainder1
        s2 = (self.color.s * numerator) // denominator + remainder2
        if self._error < 0:
            s1, s2 = s2, s1
        canvas.set(
            self._next[0], 
            self._next[1], 
            self.color.with_s(s1)
        )
        if self._error != 0:
            canvas.set(
                self._next[0] + self._main_axis * sign(self._error),
                self._next[1] + self._sub_axis * sign(self._error),
                self.color.with_s(s2)
            )
        
        return True
