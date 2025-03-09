from blessed import Terminal
term = Terminal()

# simulates standby state, ask user to press key for booting
# extends Screen
class StandbyScreen:
    def __init__(self, manager):
        self.manager = manager
        pass


    def render(self):
        print(term.home + term.clear + term.move_y(term.height // 2))
        print(term.black_on_darkkhaki(term.center('alvó üzemmód, nyomjon meg egy gombot, elvtárs.')))
               
        with(term.cbreak(), term.hidden_cursor()):
            term.inkey()
            print("indítás...")
            
        
        
        

