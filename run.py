import src.app.app as common_server

import subprocess
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def init_pencil_python():
    """
    initialize command pathing for pencil-code
    :return:
    """
    command = "source /app/pencil-code/sourceme.sh"
    try:
        result = subprocess.run(
            command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        logging.info("Command output:\n%s", result.stdout)
        if result.stderr:
            logging.warning("Command error output:\n%s", result.stderr)
    except subprocess.CalledProcessError as e:
        logging.error("Command failed with error: %s", e)
        logging.error("Command stderr: %s", e.stderr)

def run_pencil_api():
     init_pencil_python()
     server = common_server.CommonApp("9020")
     server.run_server()

if __name__ == '__main__':
    run_pencil_api()