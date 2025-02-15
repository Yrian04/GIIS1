from abc import ABC, abstractmethod

from .drawer import Drawer
from ..canvas import Canvas


class Painter(ABC):
    @abstractmethod
    def draw(self, drawer: Drawer, canvas: Canvas):
        pass
