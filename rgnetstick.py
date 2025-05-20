# title: rgnetstick
# author: Richard Sprague
# desc: A simple frontend for netstick
# site: 
# license: MIT
# version: 1.0

import pyxel
from settings_screen import SettingsScreen

WIDTH = 160
HEIGHT = 120
class App:
    def __init__(self):
        self.screen_stack = []
        self.screen_stack.append(SettingsScreen(self))
        pyxel.init(WIDTH, HEIGHT, quit_key=pyxel.KEY_NONE)
        pyxel.run(self.update, self.draw)

    def current_screen(self):
        if len(self.screen_stack) == 0:
            return None
        return self.screen_stack[-1]
    
    def exit(self):
        pyxel.quit()

    def update(self):
        self.current_screen().update()
        if self.current_screen().is_done:
            self.screen_stack.pop();
            if self.current_screen() is None:
                self.exit()

    def draw(self):
        self.current_screen().draw()

App()
