from enum import Enum

from ..abc.color import Color
from .abc.tool import Tool
from .parabola_drawer import ParabolaDrawer, ParabolaDirection


class ParabolaTool(Tool):
    def __init__(
        self,
        top: tuple[int, int],
        a: int,
        color: Color, 
        direction: ParabolaDirection,
    ):
        super().__init__()
        self.top = top
        self.a = a
        self.color = color
        self.direction = direction        
    
    def create(self):
        return ParabolaDrawer(*self.top, self.a, self.color, self.direction)

