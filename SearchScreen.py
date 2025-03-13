import Screen
import blessed
import SearchPendingScreen

term = blessed.Terminal()


class SearchScreen(Screen.Screen):
    def __init__(self, manager):
        self.manager = manager
        pass

    def render(self):
        print(term.home + term.clear)
        prompt = input(f"{term.move_x(term.width // 2) + term.move_y(term.height // 2)}kereses: ")

        if prompt:
            self.manager.transition(SearchPendingScreen.SearchPendingScreen(self.manager, prompt))

        pass
        
