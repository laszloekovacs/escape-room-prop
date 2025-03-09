from StartScreen import StartScreen


class Manager:
    def __init__(self):
        self.current_screen = StartScreen(self)
        print("stated")


    def transition(self, next_screen):
        """transition to next state. if you want to exit, transition to None"""
        if next_screen is None:
            self.current_screen = None
        else:
            self.current_screen = next_screen(self)

    def run(self):
        """runs untill current screen is set to None"""
        while self.current_screen:
            self.current_screen.render()
        print("exiting...")
