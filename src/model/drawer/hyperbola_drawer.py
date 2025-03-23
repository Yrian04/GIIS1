from ..abc.drawer import Drawer
from ...model.canvas import Canvas
from ..color import Color


class HyperbolaDrawer(Drawer):
    def __init__(
        self, 
        xc: int,
        yc: int,
        a: int,
        b: int,
        color: Color
    ):
        super().__init__()
        self.xc = xc
        self.yc = yc
        self.a = a
        self.b = b
        self.color = color
        self.x = a
        self.y = 0
        self.error = 0
    
    def draw(self, canvas):
        self._plot(canvas)
        
        errors = {
            (1, 0): self.error + self.b**2 * (2*self.x + 1),
            (0, 1): self.error - self.a**2 * (2*self.y + 1),
            (1, 1): self.error + 2*(self.b**2*self.x - self.a**2*self.y) + self.b**2 - self.a**2,   
        }
        abs_errors = {k: abs(errors[k]) for k in errors}
        
        step = dx, dy = min(abs_errors, key=abs_errors.get)
        
        self.x += dx
        self.y += dy
        
        self.error = errors[step]

        return \
            (self.xc + self.x < canvas.shape[0] or self.xc > self.x) and \
            (self.yc + self.y < canvas.shape[1] or self.yc > self.y)
    
    def _plot(self, canvas: Canvas):
        canvas.set(self.xc + self.x, self.yc + self.y, self.color)
        canvas.set(self.xc + self.x, self.yc - self.y, self.color)
        canvas.set(self.xc - self.x, self.yc + self.y, self.color)
        canvas.set(self.xc - self.x, self.yc - self.y, self.color)
