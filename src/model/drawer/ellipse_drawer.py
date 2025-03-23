from ..color import Color
from ..abc.drawer import Drawer
from ..canvas import Canvas


class EllipseDrawer(Drawer):
    def __init__(self, xc: int, yc: int, rx: int, ry: int, color: Color):
        self.xc = xc
        self.yc = yc
        self.rx = rx
        self.ry = ry
        self.color = color
        self.x = 0
        self.y = ry
        self.dx = 2 * self.ry**2 * self.x
        self.dy = 2 * self.rx**2 * self.y
        self.error = (self.ry**2 - self.rx**2 * self.ry + 
                      (self.rx**2) // 4)
        self.region = 1  # 1 - первый регион, 2 - второй

    def draw(self, canvas: Canvas) -> bool:
        if self.region == 1:
            return self.process_region1(canvas)
        elif self.region == 2:
            return self.process_region2(canvas)
        return False

    def process_region1(self, canvas: Canvas) -> bool:
        if self.dy > self.dx:  # Условие продолжения в регионе 1
            self.plot_points(canvas, self.x, self.y)

            self.dx += 2 * self.ry**2
            if self.error < 0:
                self.error += self.dx + self.ry**2
            else:
                self.y -= 1
                self.dy -= 2 * self.rx**2
                self.error += self.dx - self.dy + self.ry**2
            self.x += 1
            return True
        else:
            # Переход ко второму региону
            self.region = 2
            self.error = (self.ry**2 * (self.x + 0.5)**2 + 
                         self.rx**2 * (self.y - 1)**2 - 
                         self.rx**2 * self.ry**2)
            return self.process_region2(canvas)

    def process_region2(self, canvas: Canvas) -> bool:
        if self.y < 0:
            return False

        self.plot_points(canvas, self.x, self.y)

        self.dy -= 2 * self.rx**2
        if self.error > 0:
            self.error += self.rx**2 - self.dy
        else:
            self.x += 1
            self.dx += 2 * self.ry**2
            self.error += self.dx - self.dy + self.rx**2

        self.y -= 1
        return True

    def plot_points(self, canvas: Canvas, x: int, y: int):
        points = [
            (self.xc + x, self.yc + y),
            (self.xc - x, self.yc + y),
            (self.xc + x, self.yc - y),
            (self.xc - x, self.yc - y),
        ]
        for px, py in points:
            canvas.set(px, py, self.color)