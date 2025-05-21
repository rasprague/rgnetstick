import pyxel

BLACK = 0
WHITE = 7

class Numpad:
    def __init__(self, app, on_enter, title, text="") -> None:
        self.app = app
        self.on_enter = on_enter
        self.title = title
        self.text = text
        self.cursor_x = 0
        self.cursor_y = 0
        self.is_done = False
        self.keys = [
            ["7", "8", "9"],
            ["4", "5", "6"],
            ["1", "2", "3"],
            ["0", ".", "<-"],
        ]
        self.extra_keys = [
            "clear",
            "enter",
            "cancel",
        ]

    def exit(self):
        self.is_done = True

    def on_select(self):
        current_text = ""
        if self.cursor_y < 4:
            current_text = self.keys[self.cursor_y][self.cursor_x]
        else:
            current_text = self.extra_keys[self.cursor_y - 4]
        
        match current_text:
            case "<-":
                self.text = self.text[:-1]
            case "clear":
                self.text = ""
            case "enter":
                self.on_enter(self.title, self.text)
                self.exit()
            case "cancel":
                self.exit()
            case _: # default
                self.text = self.text + current_text

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            self.exit()
        
        if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
            if self.cursor_y > 0:
                self.cursor_y -= 1
        elif pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
            if self.cursor_y < 7 - 1:
                self.cursor_y += 1
        elif pyxel.btnp(pyxel.KEY_LEFT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
            if self.cursor_x > 0:
                self.cursor_x -= 1
        elif pyxel.btnp(pyxel.KEY_RIGHT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
            if self.cursor_x < 3 -1:
                self.cursor_x += 1

        elif pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
            self.on_select()

    def draw(self):
        pyxel.cls(BLACK)
        x = 0
        y = 0
        pyxel.text(x, y, self.title, WHITE)
        y += 8
        pyxel.text(x, y, self.text, WHITE)
        y += 16
        
        # draw keys
        for j in range(len(self.keys)):
            x = 8
            row = self.keys[j]
            for i in range(len(row)):
                u = 0
                v = 0
                w = 8
                h = 8
                if (i == self.cursor_x and j == self.cursor_y):
                    v = 8
                pyxel.blt(x, y, 0, u, v, w, h)
                pyxel.text(x+1, y+1, row[i], BLACK)
                x += 8
            y += 8
        # draw extra keys
        y += 8
        for i in range(len(self.extra_keys)):
            x = 8
            u = 8
            v = 0
            w = 24
            h = 8
            if i == self.cursor_y - 4:
                v = 8
            pyxel.blt(x, y, 0, u, v, w, h)
            pyxel.text(x+1, y+1, self.extra_keys[i], BLACK)
            y += 8