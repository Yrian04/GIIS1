from abc import ABC, abstractmethod

from ...model.abc.tool import Tool
from ...view.abc.view import View


class ToolManager(ABC):
    @abstractmethod
    def configure(self, view: View) -> Tool:
        pass
