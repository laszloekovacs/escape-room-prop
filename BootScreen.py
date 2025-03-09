from blessed import Terminal
from Screen import Screen
import time

term = Terminal()


class BootScreen(Screen):
    def __init__(self, manager):
        super().__init__(manager)

    def render(self):
        print(term.home + term.clear)
        
        with(term.cbreak(), term.hidden_cursor()):
            print(term.move_y(term.height // 2))
            print(term.center("Booting..."))
            time.sleep(1)
            print(term.move_down(1))
            print(term.center("Loading kernel..."))
            time.sleep(1)
            print(term.move_down(1))
            print(term.center("Starting services..."))
            time.sleep(1)
            print(term.move_down(1))
            print(term.center("Done."))
            time.sleep(1)
        
        self.manager.transition(None)
