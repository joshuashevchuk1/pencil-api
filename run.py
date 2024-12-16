import src.app.app as common_server

import logging
import config.config as cfg

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def setup_config():
    config = cfg.Config()
    config.setup_config()

def run_pencil_api():
     setup_config()
     server = common_server.CommonApp("9020")
     server.run_server()

if __name__ == '__main__':
    run_pencil_api()