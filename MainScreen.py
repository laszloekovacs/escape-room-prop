import blessed
import Screen
from term_image.image import from_file
import StandbyScreen
import SearchScreen

#import StandbyScreen

# main menu. this should render a logo and a menu to select submenus



term = blessed.Terminal()

# simulates standby state, ask user to press key for booting
# extends Screen
class MainScreen(Screen.Screen):
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
                    self.manager.transition(StandbyScreen.StandbyScreen(self.manager))
                  
                elif key.name == "KEY_ENTER":
                    # go to selected screen
                    if self.options[self.selection] == "keresés":
                        self.manager.transition(SearchScreen.SearchScreen(self.manager))
                    print("action")
