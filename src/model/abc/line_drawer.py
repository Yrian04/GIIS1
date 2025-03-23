from abc import ABC

from ..color import Color
from .drawer import Drawer


class LineDrawer(Drawer, ABC):
    def __init__(
        self,
        start: tuple[int, int],
        end: tuple[int, int],
        color: Color
    ):
        self.start = start
        self.end = end
        self.color = color
        