import subprocess
import os

class Netstick:
    def __init__(self):
        self.path_to_netstick = "%s/netstick/netstick" % os.path.dirname(__file__)
        os.chmod(self.path_to_netstick, 755) # make sure netstick is executable
        self.netstick_process = None

    def start(self, input_device, server_address, server_port):
        self.netstick_process = subprocess.Popen([self.path_to_netstick, input_device, server_address, server_port])

    def stop(self):
        if self.netstick_process:
            self.netstick_process.terminate()
            self.netstick_process = None
