from .color import Color


class Canvas:
    def __init__(self, shape: tuple[int, int]):
        self.callback = None
        self._shape = shape

    @property
    def shape(self):
        return self._shape

    def set(self, x: int, y: int, color: Color):
        if self.callback is not None:
            self.callback(x, y, color)

    def get(self, x: int, y: int) -> Color:
        return self.matrix[x, y]
    