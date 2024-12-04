import os

import src.app.app as common_server

def init_pencil_python():
    os.system("source /app/pencil-code/sourceme.sh")

def run_flask_app():
     server = common_server.CommonApp("9020")
     server.run_server()

if __name__ == '__main__':
    run_flask_app()