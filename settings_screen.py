import pyxel
from pyxel_menu import PyxelMenu
import json
import os
from pathlib import Path
from netstick import Netstick
from device_list import DeviceList
from menu_numpad import MenuNumpad
from numpad import Numpad
from controller_screen import ControllerScreen

BLACK = 0
WHITE = 7

class SettingsScreen():
    def __init__(self, app):
        self.app = app
        self.is_done = False
        self.netstick = Netstick()
        self.settings = {
            "INPUT_DEVICE" : "",
            "SERVER_IP" : "",
            "SERVER_PORT" : "1337"
        }
        self.settings_dir = "%s/.local/share/rgnetstick" % str(Path.home())
        try:
            os.makedirs(self.settings_dir)
        except Exception as e:
            pass
        self.settings_path = "%s/settings.json" % self.settings_dir
        self.load_settings()

        self.current_text = ''
        self.current_pos = ''

        x = 0
        y = 24
        self.menu = PyxelMenu(x, y, limit=10)
        self.refresh_menu_options()

    def save_settings(self):
        with open(self.settings_path, "w") as file:
            file.write(json.dumps(self.settings, indent=4))

    def load_settings(self):
        try:
            with open(self.settings_path, "r") as file:
                self.settings = json.load(file)
        except FileNotFoundError:
            pass

    def exit(self):
        self.save_settings() 
        self.is_done = True

    def refresh_menu_options(self):
        menu_options = [
            "INPUT_DEVICE: %s" % self.settings["INPUT_DEVICE"],
            "SERVER_IP: %s" % self.settings["SERVER_IP"], 
            "SERVER_PORT: %s" % self.settings["SERVER_PORT"], 
            "start",
            "controller test only",
            "quit",
        ]
        self.menu.set_options(menu_options)

    def on_enter_numpad(self, name, value):
        self.settings[name] = value
        self.refresh_menu_options()

    def on_select(self):
        match self.current_pos:
            case 0: # input device
                self.app.screen_stack.append(DeviceList(self.app, on_enter=self.on_enter_numpad, title="INPUT_DEVICE", text=self.settings["INPUT_DEVICE"]))
            case 1: # server ip
                #self.app.screen_stack.append(MenuNumpad(self.app, on_enter=self.on_enter_numpad, title="SERVER_IP", text=self.settings["SERVER_IP"]))
                self.app.screen_stack.append(Numpad(self.app, on_enter=self.on_enter_numpad, title="SERVER_IP", text=self.settings["SERVER_IP"]))
            case 2: # server port
                #self.app.screen_stack.append(MenuNumpad(self.app, on_enter=self.on_enter_numpad, title="SERVER_PORT", text=self.settings["SERVER_PORT"]))
                self.app.screen_stack.append(Numpad(self.app, on_enter=self.on_enter_numpad, title="SERVER_PORT", text=self.settings["SERVER_PORT"]))
            case 3: # start
                self.app.screen_stack.append(ControllerScreen(settings=self.settings))
            case 4: # controller test only
                self.app.screen_stack.append(ControllerScreen(settings=self.settings, start_netstick=False))
            case 5: # quit
                self.exit()
            case _: # default
                pass

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
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
        pyxel.text(x, y, "RGNETSTICK - a netstick frontend", WHITE)
        self.menu.draw()
