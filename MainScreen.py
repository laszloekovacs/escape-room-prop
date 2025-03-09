from blessed import Terminal
from Screen import Screen
from term_image.image import from_file

#import StandbyScreen

# main menu. this should render a logo and a menu to select submenus



term = Terminal()

# simulates standby state, ask user to press key for booting
# extends Screen
class MainScreen(Screen):
    options = ["ügynök dokumentumok", "nukleáris arzenál", "keresés", "jelentések"]
    selection = 0

    def __init__(self, manager):
        super().__init__(manager)


    def render(self):
        with term.cbreak(), term.hidden_cursor():
            print(term.home + term.clear)

            image = from_file("./images/vakond.png")
            print(image)
            #print(term.move_y(term.height) + "hello")

            menuline = ""

            for i, option in enumerate(self.options):
                if i == self.selection:
                    menuline += term.reverse(option) + " "
                else:
                    menuline += option + " "
                
            print(term.move_y(term.height-1) + menuline)
                    
            key = term.inkey()

            if key:
                if key.name == "KEY_LEFT":
                    self.selection = (self.selection - 1) % len(self.options)
                elif key.name == "KEY_RIGHT":
                    self.selection = (self.selection + 1) % len(self.options)

                elif key.name == "KEY_F1":
                    print("exiting")
                    # TODO: fix this abhorent code
                    from StandbyScreen import StandbyScreen
                    self.manager.transition(StandbyScreen)

                elif key.name == "KEY_ENTER":
                    # go to selected screen
                    print("action")
