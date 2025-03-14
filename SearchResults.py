import blessed
import Screen
from term_image.image import from_file


codeA = "Tell me why"
resultA = "5435"



term = blessed.Terminal()

class SearchResults(Screen.Screen):
    def __init__(self, manager, query):
        super().__init__(manager)
        self.query = query


    def render(self):
        print(term.home + term.clear + term.move_y(term.height // 2))

        
        if self.query:
            if self.query.lower() == codeA.lower():
                print(term.center(resultA))

        term.inkey()
