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
        config = cfg.Config(path="../config")
        simulation_dir = config.get("simulations")

        self.assertEqual(simulation_dir,"simulations")

    def test_it_should_get_the_example_path(self):
        config = cfg.Config(path="../config")
        simulation_dir = config.get("example_dir")

        self.assertEqual(simulation_dir,"examples")

    def test_it_should_get_the_api_path(self):
        config = cfg.Config(path="../config")
        simulation_dir = config.get("api_path")

        self.assertEqual(simulation_dir, "/app/pencil-code/python/pencil-api/")



