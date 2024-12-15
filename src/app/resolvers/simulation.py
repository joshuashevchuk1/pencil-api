
import os

from numpy.distutils.command.config import config

import config.config as cfg


class SimulationResolver:
    """
    resolves specific pencil commands for the pencil simulation
    """
    def __init__(self):
        self.file_name = None
        self.config = cfg.Config()
        self.simulation_dir = self.config.get("simulation_dir")
        return

    def set_file_name(self,file_name):
        self.file_name = file_name

    def build(self):
        os.system("pc_build " + "./" + str(self.simulation_dir))
        return

    def start(self):
        os.system("pc_start " + "./" + str(self.simulation_dir))
        return

    def run(self):
        os.system("pc_run " + "./" + str(self.simulation_dir))
        return