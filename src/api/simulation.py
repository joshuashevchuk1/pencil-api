
import src.app.resolvers.simulation as simulaton

class SimulationHandler:
    """
    handlers specific pencil commands for the pencil simulation
    """
    def __init__(self, app):
        self.app = app
        return

    # runs pc_build as GET
    def build_sim(self,sim_name):
        sr = simulaton.SimulationResolver()
        sr.set_sim(sim_name)
        sr.build()
        return

    # runs pc_start as GET
    def start_sim(self, sim_name):
        sr = simulaton.SimulationResolver()
        sr.set_sim(sim_name)
        sr.run()
        return

    # runs pc_run as GET
    def run_sim(self, sim_name):
        sr = simulaton.SimulationResolver()
        sr.set_sim(sim_name)
        sr.run()
        return