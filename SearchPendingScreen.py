import Screen
import blessed

term = blessed.Terminal()


class SearchPendingScreen(Screen.Screen):
    def __init__(self, manager, prompt = ""):
        self.manager = manager
        self.prompt = prompt
        pass

    def render(self):
        print(term.clear + term.home)
        print(f"searching for: {self.prompt}")
        term.inkey()

        pass
        
