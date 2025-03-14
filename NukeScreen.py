import blessed
import MainScreen
import Screen
from term_image.image import from_file

term = blessed.Terminal()

class NukeScreen(Screen.Screen):
    def __init__(self, manager):
        super().__init__(manager)
        self.imgA = from_file("./images/cardA.jpg")
        self.imgB = from_file("./images/cardB.jpg")
        self.blink = True


    def render(self):
        print(term.home + term.clear)
        
        if self.blink:
            self.imgA.draw(h_align="center", v_align="middle")        
        else:
            self.imgB.draw(h_align="center", v_align="middle")

        self.blink = not self.blink

        print("\nHiba: kártya olvasó nincs csatlakoztatva\nA folytatáshoz helyezze be az indítókártyát\nNyomjon meg bármilyen billentyűt")        
        prompt = term.inkey(1)
        
        if prompt :
            self.manager.transition(MainScreen.MainScreen(self.manager))
