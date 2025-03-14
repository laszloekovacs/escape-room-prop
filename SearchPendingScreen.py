import random
import Screen
import blessed
from term_image.image import from_file
import time 
import os

import SearchResults

term = blessed.Terminal()

class SearchPendingScreen(Screen.Screen):
    def __init__(self, manager, prompt = ""):
        self.manager = manager
        self.prompt = prompt
        pass

    def render(self):
        with term.cbreak(), term.hidden_cursor():
            start_time = time.time()

            blink = True

            path = "./images/slides/"
            # read all image names into an array from images/slides
            dir = os.listdir(path)

            # choose a random starting image
            index = random.randint(0, len(dir) - 1)

            # show the images until 4 seconds pass                
            while time.time() - start_time < 6:
                print(term.clear + term.home)
                
                image = from_file(path + dir[index])
                image.draw(h_align="center", v_align="middle")
                index = (index + 1) % len(dir)

                title = term.bold("kereses folyamatban: " + self.prompt if blink == True else "")
                message = term.move_y(term.height // 2) + term.black_on_darkkhaki(term.center(title))
                print(message)
                
                blink = not blink

                # wait for x seconds
                time.sleep(0.6)

            #at the end, go to searchResult screen    
            self.manager.transition(SearchResults.SearchResults(self.manager, self.prompt))
            pass    

                
