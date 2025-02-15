from abc import ABC, abstractmethod

import tkinter as tk

from .view import View
import config


class MenuItem(ABC):
    @abstractmethod
    def create(self, menu: tk.Menu, label: str, tag: str):
        pass


class Command(MenuItem):
    def create(self, menu, label: str, command):
        menu.add_command(label=label, command=command)


class CheckButton(MenuItem):
    def create(self, menu, label, command):
        menu.add_checkbutton(label=label, command=command)


class Window(tk.Tk, View, ABC):
    def _build_menu(self) -> tk.Menu:
        def process_item(
            menu_struct: dict,
            preffix = 'Main'
        ) -> tuple[tk.Menu, dict[str, tk.Menu]]:
            menu = tk.Menu(tearoff=0)
            for item in menu_struct:
                tag = f'{preffix}.{item}'
                item_struct = menu_struct[item]
                if isinstance(item_struct, MenuItem):
                    self.add_tag(tag)
                    item_struct.create(menu, item, lambda t=tag: self._notify_tag(t))
                else:
                    item_menu = process_item(item_struct, preffix=tag)
                    menu.add_cascade(label=item, menu=item_menu)
            return menu
        return process_item(config.main_menu_struct)

    def input(self, messange):
        event_str = '<Button-1>'
        
        self.show_info(messange)
        
        x: int = None
        y: int = None
        input_wait_var = tk.IntVar(self, 0)
        def input_handler(e: tk.Event):
            nonlocal x, y, input_wait_var
            x, y = e.x, e.y
            input_wait_var.set(1)

        funcid = self.canvas.bind(event_str, input_handler, '+')
        self.wait_variable(input_wait_var)
        self.canvas.unbind(event_str, funcid)
        self.show_info(config.start_info_str)
        return x // config.cell_size, y // config.cell_size

    