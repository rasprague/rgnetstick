import pyxel
from pyxel_menu import PyxelMenu

BLACK = 0
WHITE = 7

class MenuNumpad:
    def __init__(self, app, on_enter, title, text=""):
        self.app = app
        self.on_enter = on_enter
        self.title = title
        self.text = text
        self.is_done = False
        self.current_pos = ""
        self.current_text = ""
        menu_options = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "del", "clear", "enter", "cancel"]
        x = 0
        y = 32
        self.menu = PyxelMenu(x, y, menu_options, limit=10)

    def exit(self):
        self.is_done = True

    def on_select(self):
        match self.current_text:
            case "del":
                self.text = self.text[:-1]
            case "clear":
                self.text = ""
            case "enter":
                self.on_enter(self.title, self.text)
                self.exit()
            case "cancel":
                self.exit()
            case _: # default
                self.text = self.text + self.current_text

    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            self.exit()
        
        if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
            self.menu.move_up()
        elif pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
            self.menu.move_down()

        if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
            self.current_pos = self.menu.get_current_pos()
            self.current_text = self.menu.get_current_text()
            self.on_select()

    def draw(self):
        pyxel.cls(BLACK)
        x = 8
        y = 8
        pyxel.text(x, y, self.title, WHITE)
        y += 8
        pyxel.text(x, y, self.text, WHITE)
        self.menu.draw()
