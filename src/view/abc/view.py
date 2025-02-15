from abc import ABC, abstractmethod
from typing import Callable

from tkinter import Event

from .messange import Messange
from ...abc.event import Event
from ...abc.publisher import Publisher

class View(Publisher, ABC):
    @abstractmethod
    def input(self, messange: Messange):
        pass
