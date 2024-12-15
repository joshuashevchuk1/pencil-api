
import os

import config.config as cfg


class SimulationResolver:
    """
    resolves specific pencil commands for the pencil simulation
    """
    def __init__(self):
        self.sim = None
        self.config = cfg.Config()
        self.simulations = self.config.get("simulations")
        self.api_path = self.config.get("api_path")
        return

    def set_sim(self, sim):
        self.sim = sim

    def build(self):
        os.chdir(str(self.api_path) + str(self.simulations) + "/" + str(self.sim))
        os.system("pc_build " + "/app/pencil-code/python/pencil-api" + str(self.simulations))
        return

    def start(self):
        os.chdir(str(self.api_path) + str(self.simulations) + "/" + str(self.sim))
        os.system("pc_start " + "/app/pencil-code/python/pencil-api" + str(self.simulations))
        return

    def run(self):
        os.chdir(str(self.api_path) + str(self.simulations) + "/" + str(self.sim))
        os.system("pc_run " + "/app/pencil-code/python/pencil-api" + str(self.simulations))
        return