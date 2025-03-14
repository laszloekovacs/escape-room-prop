import blessed
import Screen
from term_image.image import from_file

term = blessed.Terminal()

class NukeScreen(Screen.Screen):
    def __init__(self, manager):
        super().__init__(manager)
        


    def render(self):
        print(term.home + term.clear)

        img = from_file("./images/nuke_card.gif")
        img.draw(h_aling="center", v_align="middle", animate=True, repeat=-1)        

        print("A folytatáshoz helyezze be az indítókártyát")        
        term.inkey()
