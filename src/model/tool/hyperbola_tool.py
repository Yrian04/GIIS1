from ..color import Color
from ..abc.tool import Tool
from ..drawer.hyperbola_drawer import HyperbolaDrawer


class HyperbolaTool(Tool):
    def __init__(
        self,
        center: tuple[int, int],
        a: int,
        b: int,
        color: Color
    ):
        super().__init__()
        self.center = center
        self.a = a
        self.b = b
        self.color = color

    def create(self):
        return HyperbolaDrawer(
            self.center[0],
            self.center[1],
            self.a,
            self.b,
            self.color
        )