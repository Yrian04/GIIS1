from typing import Literal, TypeAlias

from ..abc.color import Color
from ..utils import sign
from .abc.drawer import Drawer
from .canvas import Canvas


ParabolaDirection: TypeAlias = Literal['up', 'right', 'down', 'left']


class ParabolaDrawer(Drawer):
    def __init__(
        self,
        x0: int,
        y0: int,
        a: int,
        color: Color,
        direction: ParabolaDirection
    ):
        self.x0 = x0
        self.y0 = y0
        self.a = a
        self.color = color
        self.direction = direction
        
        self.x = 0
        self.y = 0
        self.error = 0

    def draw(self, canvas: Canvas) -> bool:
        self._plot(canvas)
        
        errors = {
            (1, 0): self.error - 2 * self.x - 1,
            (0, 1): self.error + self.a,
            (1, 1): self.error - 2 * self.x + self.a - 1,   
        }
        abs_errors = {k: abs(errors[k]) for k in errors}
        
        step = dx, dy = min(abs_errors, key=abs_errors.get)
        
        self.x += dx
        self.y += dy * sign(self.a)
        
        self.error = errors[step]
        
        return \
            (self.x0 + self.x < canvas.shape[0] or self.x0 > self.x) and \
            (self.y0 + self.y < canvas.shape[1] or self.y0 > self.y)
    
    def _plot(self, canvas: Canvas):
        def plot(x, y):
                canvas.set(self.x0 + x, self.y0 + y, self.color)
                
        match self.direction:
            case 'up':
                plot(self.x, self.y)
                plot(-self.x, self.y)
            case 'right':
                plot(self.y, self.x)
                plot(self.y, -self.x)
            case 'down':
                plot(self.x, -self.y)
                plot(-self.x, -self.y)
            case 'left':
                plot(-self.y, self.x)
                plot(-self.y, -self.x)
