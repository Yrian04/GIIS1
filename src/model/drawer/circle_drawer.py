from ..color import Color
from ..abc.drawer import Drawer
from ..canvas import Canvas


class CircleDrawer(Drawer):
    def __init__(self, xc: int, yc: int, radius: int, color: Color):
        self.xc = xc
        self.yc = yc
        self.radius = radius
        self.color = color
        self.x = 0
        self.y = radius
        self.d = 3 - 2 * radius
        self.finished = False

    def draw(self, canvas: Canvas) -> bool:
        if self.finished:
            return False

        if self.x > self.y:
            self.finished = True
            return False

        self.plot_points(canvas, self.x, self.y)

        if self.d < 0:
            self.d += 4 * self.x + 6
        else:
            self.d += 4 * (self.x - self.y) + 10
            self.y -= 1
        self.x += 1

        return True

    def plot_points(self, canvas: Canvas, x: int, y: int):
        points = [
            (self.xc + x, self.yc + y),
            (self.xc - x, self.yc + y),
            (self.xc + x, self.yc - y),
            (self.xc - x, self.yc - y),
            (self.xc + y, self.yc + x),
            (self.xc - y, self.yc + x),
            (self.xc + y, self.yc - x),
            (self.xc - y, self.yc - x),
        ]
        for px, py in points:
            canvas.set(px, py, self.color)