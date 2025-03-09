from blessed import Terminal
from BootScreen import BootScreen
from Screen import Screen

term = Terminal()

# simulates standby state, ask user to press key for booting
# extends Screen
class StandbyScreen(Screen):
    def __init__(self, manager):
        super().__init__(manager)


    def render(self):
        print(term.home + term.clear + term.move_y(term.height // 2))
        print(term.black_on_darkkhaki(term.center('alvó üzemmód, nyomjon meg egy gombot, elvtárs.')))
               
        with(term.cbreak(), term.hidden_cursor()):
            term.inkey()
            print("indítás...")
            self.manager.transition(BootScreen)
            
        
        
        

