
import os
import config.config as cfg

class SimulationResolver:
    """
    resolves specific pencil commands for the pencil simulation
    """
    def __init__(self):
        self.file_name = None
        self.config = cfg.Config()
        return

    def set_file_name(self,file_name):
        self.file_name = file_name

    def build(self):
        os.system("pc_build")

        return

    def start(self):
        return

    def run(self):
        return