
import os
import sys

class SimulationResolver:
    """
    resolves specific pencil commands for the pencil simulation
    """
    def __init__(self):
        self.file_name = None
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