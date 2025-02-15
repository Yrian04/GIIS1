from abc import ABC, abstractmethod

from ...abc.color import Color
from .view import View


class MainView(View, ABC):
    @abstractmethod
    def set_cell(self, x: int, y: int, color: Color):
        pass

    @abstractmethod
    def on_change_debug_mode(self, mode: bool):
        pass

    @abstractmethod
    def debug_wait(self):
        pass
    
    @abstractmethod
    def show_info(self, messange):
        pass
