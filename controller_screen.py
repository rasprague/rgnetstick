import pyxel
from netstick import Netstick

BLACK = 0
WHITE = 7

class ControllerScreen:
    def __init__(self, settings, start_netstick=True):
        self.is_done = False

        self.netstick = None
        if start_netstick:
            self.netstick : Netstick = Netstick()
            self.netstick.start("/dev/input/%s" % settings["INPUT_DEVICE"], settings["SERVER_IP"], settings["SERVER_PORT"])

        self.digital_keys = [
            (pyxel.GAMEPAD1_BUTTON_DPAD_UP, "DPAD_UP"),
            (pyxel.GAMEPAD1_BUTTON_DPAD_DOWN, "DPAD_DOWN"),
            (pyxel.GAMEPAD1_BUTTON_DPAD_LEFT, "DPAD_LEFT"),
            (pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT, "DPAD_RIGHT"),
            (pyxel.GAMEPAD1_BUTTON_BACK, "BACK"),
            (pyxel.GAMEPAD1_BUTTON_START, "START"),
            (pyxel.GAMEPAD1_BUTTON_A, "A"),
            (pyxel.GAMEPAD1_BUTTON_B, "B"),
            (pyxel.GAMEPAD1_BUTTON_X, "X"),
            (pyxel.GAMEPAD1_BUTTON_Y, "Y"),
            (pyxel.GAMEPAD1_BUTTON_LEFTSHOULDER, "LEFTSHOULDER"),
            (pyxel.GAMEPAD1_BUTTON_RIGHTSHOULDER, "RIGHTSHOULDER"),
            (pyxel.GAMEPAD1_BUTTON_LEFTSTICK, "LEFTSTICK"),
            (pyxel.GAMEPAD1_BUTTON_RIGHTSTICK, "RIGHTSTICK"),
        ]
        self.analog_keys = [
            (pyxel.GAMEPAD1_AXIS_LEFTX, "LEFTX"),
            (pyxel.GAMEPAD1_AXIS_LEFTY, "LEFTY"),
            (pyxel.GAMEPAD1_AXIS_RIGHTX, "RIGHTX"),
            (pyxel.GAMEPAD1_AXIS_RIGHTY, "RIGHTY"),
            (pyxel.GAMEPAD1_AXIS_TRIGGERLEFT, "TRIGGERLEFT"),
            (pyxel.GAMEPAD1_AXIS_TRIGGERRIGHT, "TRIGGERRIGHT"),
        ]

    def exit(self):
        if self.netstick:
            self.netstick.stop()
            self.netstick = None
        self.is_done = True

    def update(self):
        if pyxel.btn(pyxel.KEY_Q) or (pyxel.btn(pyxel.GAMEPAD1_BUTTON_BACK) and pyxel.btn(pyxel.GAMEPAD1_BUTTON_START) and pyxel.btn(pyxel.GAMEPAD1_BUTTON_LEFTSHOULDER) and pyxel.btn(pyxel.GAMEPAD1_BUTTON_RIGHTSHOULDER) and pyxel.btnv(pyxel.GAMEPAD1_AXIS_TRIGGERLEFT) and pyxel.btnv(pyxel.GAMEPAD1_AXIS_TRIGGERRIGHT)):
            self.exit()
                  
    def draw(self):
        pyxel.cls(BLACK)
        pyxel.text(0, 0, "(BACK+START+L1+R1+L2+R2 to exit)", WHITE)
        x = 0
        y = 8
        for i in range(len(self.digital_keys)):
            k = self.digital_keys[i]
            # if pyxel.btn(k[0]):
            #     pyxel.text(x, y, k[1], WHITE)
            status = "x" if pyxel.btn(k[0]) else ""
            pyxel.text(x, y, "%s %s" % (k[1], status), WHITE)
            y += 8
        x = 80
        y = 8
        for i in range(len(self.analog_keys)):
            k = self.analog_keys[i]
            btnv = pyxel.btnv(k[0])
            pyxel.text(x, y, "%s %d" % (k[1], btnv), WHITE)
            y += 8
        y += 16
        if self.netstick:
            status = self.netstick.netstick_process.poll()
            if status is None:
                status = "running"
            pyxel.text(x, y, "netstick status: \n%s" % status, WHITE)
            y += 16
            pyxel.text(x, y, "netstick pid: \n%d" % self.netstick.netstick_process.pid, WHITE)
