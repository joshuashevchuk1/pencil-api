import logging
import sys
import unittest
import config.config as cfg

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)


class TestConfig(unittest.TestCase):
    def test_it_should_get_the_simulation_path(self):
        config = cfg.Config()
        simulation_dir = config.get("simulation_dir")

        self.assertEqual(simulation_dir,"simulation")


