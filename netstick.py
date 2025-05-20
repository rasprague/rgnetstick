import subprocess
import os

class Netstick:
    def __init__(self):
        self.path_to_netstick = "%s/netstick/netstick" % os.path.dirname(__file__)
        self.netstick_process = None
        print(self.path_to_netstick)

    def start(self, input_device, server_address, server_port):
        self.netstick_process = subprocess.Popen([self.path_to_netstick, input_device, server_address, server_port])

    def stop(self):
        if self.netstick_process:
            self.netstick_process.terminate()
            self.netstick_process = None
