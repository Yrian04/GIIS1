from abc import ABC
from typing import Callable

from .event import Event


class Publisher(ABC):
    def __init__(self):
        self._callbacks: dict[str, list[Callable[[Event], None]]] = {}

    def add_tag(self, tag: str) -> None:
        self._callbacks[tag] = []

    def remove_tag(self, tag: str) -> None:
        self.check_tag(tag)
        del self._callbacks[tag]

    def subscribe(self, tag: str, callback: Callable[[Event], None]) -> None:
        self.check_tag(tag)
        self._callbacks[tag].append(callback)

    def unsubscribe(self, tag: str, callback: Callable[[Event], None]) -> None:
        self.check_tag(tag)
        if callback in (event_callbacks := self._callbacks[tag]):
            event_callbacks.remove(callback)

    def _notify(self, event: Event) -> None:
        self.check_tag(tag := event.tag)
        for callback in self._callbacks[tag]:
            callback(event)
        
    def _notify_tag(self, tag: str) -> None:
        event = Event(tag, self)
        self._notify(event)

    def check_tag(self, tag: str) -> None:
        if tag not in self._callbacks:
            raise ValueError(f'This publisher do not support {tag} event tag')
