import MainScreen
import Screen
import blessed

term = blessed.Terminal()


class ForbiddenScreen(Screen.Screen):
    def __init__(self, manager):
        self.manager = manager
        pass

    def render(self):
        with term.cbreak(): 
            print(term.home + term.clear),
            print(term.move_y(term.height //2) + term.center(term.black_on_darkkhaki("hozzáférés megtagadva")))
            term.inkey()
            self.manager.transition(MainScreen.MainScreen(self.manager))
        


        
