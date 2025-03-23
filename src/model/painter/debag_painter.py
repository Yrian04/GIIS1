from typing import Callable

from ..abc.painter import Painter


class DebagPainter(Painter):
    def __init__(self, callback: Callable[[None], bool], n=2):
        super().__init__()
        self._callback = callback
        self.n = n

    def draw(self, drawer, canvas):
        i = -1
        def stop():
            nonlocal i
            i += 1
            return True if i % self.n != 0 else self._callback()

        while drawer.draw(canvas) and stop():
            pass
