from blessed import Terminal
from Screen import Screen
from MainScreen import MainScreen
import time

term = Terminal()


class BootScreen(Screen):
    def __init__(self, manager):
        super().__init__(manager)

    def render(self):
        print(term.home + term.clear)
        
        with(term.cbreak(), term.hidden_cursor()):
            print(term.move_x(5) + "T: 1984.03.22 - 20:13")
            print(term.move_xy(5, 2) + "rendszer indítása\n")
            time.sleep(1)
            print(term.move_x(5) + "\tRAM\t\tROM\t\tHDD")
            print(term.move_x(5) + "\t64kb\t\t256K\t\t24Mb\n")
            
            time.sleep(1)
            print(term.move_x(5) + "hálózat")
            print(term.move_x(5) + "ok")
            print(term.move_x(5) + "terminál")
            print(term.move_x(5) + "ok\n")
            
            time.sleep(0.4)
            print(term.move_x(5) + "kgb megfigyelő hálózat")
            print(term.move_x(5) + "csatlakozás sikertelen\n")

            print(term.move_x(5) + "bejelentkezés...")
            
            time.sleep(1.8)
        
        self.manager.transition(MainScreen)
