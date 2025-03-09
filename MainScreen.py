# main menu. this should render a logo and a menu to select submenus

from blessed import Terminal

from Screen import Screen

term = Terminal()

# simulates standby state, ask user to press key for booting
# extends Screen
class MainScreen(Screen):
    def __init__(self, manager):
        super().__init__(manager)


    def render(self):
        print("main")

        with(term.cbreak(), term.hidden_cursor()):
            term.inkey()
            print("indítás...")
            self.manager.transition(None)
            
        
        
        

