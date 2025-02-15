from abc import ABC, abstractmethod

from ..canvas import Canvas


class Drawer(ABC):
    @abstractmethod
    def draw(self, canvas: Canvas) -> bool:
        pass
