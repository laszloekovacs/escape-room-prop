class AppManager:
    def __init__(self):
        #self.current_screen = StartScreen(self)
        print("stated")


    def transition(self, next_state):
        """transition to next state."""
        if next_state is None:
            self.current_state = None
        else:
            self.current_state = next_state(self)

    def run(self):
        print("running")
