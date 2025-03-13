import blessed
import BootScreen
import Screen
from term_image.image import from_file


term = blessed.Terminal()

# simulates standby state, ask user to press key for booting
# extends Screen
class StandbyScreen(Screen.Screen):
    def __init__(self, manager):
        super().__init__(manager)


    def render(self):
        print(term.clear)
        image = from_file("./images/hns.png")
        print(image)
        print(term.home + term.move_y(term.height // 2))
        print(term.gray(term.center('alvó üzemmód, nyomjon meg egy gombot, elvtárs.')))
               
        with(term.cbreak(), term.hidden_cursor()):
            term.inkey()
            print("indítás...")
            self.manager.transition(BootScreen.BootScreen(self.manager))
