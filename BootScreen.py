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
            print(term.move_xy(5, 2) + "rendszer indítása\n")
            time.sleep(1)
            print(term.move_x(5) + "ram")
            print(term.move_x(5) + "64kb")
            print(term.move_x(5) + "rom")
            print(term.move_x(5) + "256kb\n")
            time.sleep(1)
            print(term.move_x(5) + "hálózat")
            print(term.move_x(5) + "ok\n")
            print(term.move_x(5) + "terminál")
            print(term.move_x(5) + "ok\n")
            time.sleep(0.4)
            print(term.move_x(5) + "kgb megfigyelő")
            print(term.move_x(5) + "csatlakozás...")         
            
            time.sleep(1)
        
        self.manager.transition(None)
