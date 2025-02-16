import math

from ..abc.color import Color
from .abc.tool import Tool
from .circle_drawer import CircleDrawer


class CircleTool(Tool):
    def __init__(
        self,
        center: tuple[int, int],
        point: tuple[int, int],
        color: Color
    ):
        super().__init__()
        self.color = color
        self.center = center
        delta = center[0] - point[0], center[1] - point[1]
        self.radius = int(math.sqrt(delta[0] ** 2 + delta[1] ** 2)) #TODO

    def create(self):
        return CircleDrawer(*self.center, self.radius, self.color)
