from abc import ABC, abstractmethod

from .drawer import Drawer


class Tool(ABC):
    @abstractmethod
    def create(self) -> Drawer:
        pass 
