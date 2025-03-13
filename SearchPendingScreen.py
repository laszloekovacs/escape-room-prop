import Screen
import blessed
from term_image.image import from_file

term = blessed.Terminal()


class SearchPendingScreen(Screen.Screen):
    def __init__(self, manager, prompt = ""):
        self.manager = manager
        self.prompt = prompt
        pass

    def render(self):
        print(term.clear + term.home)
        message = term.move_y(term.height // 2) + term.black_on_darkkhaki(term.center("kereses: " + self.prompt))

        image = from_file("./images/slides/notes.png")
        image.draw(h_align="center", v_align="middle")

        print(message)

        term.inkey()
        pass
        
