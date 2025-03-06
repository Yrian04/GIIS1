from abc import ABC

import config
from ...abc.color import Color
from .drawer import Drawer


class LineDrawer(Drawer, ABC):
    def __init__(
        self,
        start: tuple[int, int],
        end: tuple[int, int],
        color: Color = config.standard_color
    ):
        self.start = start
        self.end = end
        self.color = color
        