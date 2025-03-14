import blessed
import MainScreen
import Screen
from term_image.image import from_file


codes = {
    "tell me why": "5435",
    "egy amerikai párizsban": "32",
    "durch berlin": "23",
    "katyusa": "2",
}



term = blessed.Terminal()

class SearchResults(Screen.Screen):
    def __init__(self, manager, query):
        super().__init__(manager)
        self.query = query

    def render(self):
        with term.cbreak():
            print(term.home + term.clear + term.move_y(term.height // 2))
            
            #if prompt is in the keys
            if self.query.lower() in codes:
                print(term.move_y(term.height // 2) + term.center(codes[self.query.lower()]))

            else:
                print(term.center("nincs találat"))

            term.inkey()
            self.manager.transition(MainScreen.MainScreen(self.manager))
