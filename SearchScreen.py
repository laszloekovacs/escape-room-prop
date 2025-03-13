import Screen
import blessed

term = blessed.Terminal()


class SearchScreen(Screen.Screen):
    def __init__(self, manager):
        self.manager = manager
        pass

    def render(self):
        print(term.home + term.clear)
        input(f"${term.move_x(term.width // 2) + term.move_y(term.height // 2)}kereses: ")
        pass
        
