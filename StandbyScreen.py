from blessed import Terminal
term = Terminal()

# simulates standby state, ask user to press key for booting
# extends Screen
class StandbyScreen:
    def __init__(self, manager):
        self.manager = manager
        pass


    def render(self):
        print(term.home + term.clear)
               
        term.inkey()
        pass
        
        

