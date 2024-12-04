
from flask import request, jsonify
import resolvers.pencil_init as rpi

class PencilInit:
        def __init__(self, app):
            self.app = app
            self.data = None
            return

        def post_start_init(self):

            self.data = request.get_json()
            self.write_init("start")

            return jsonify({"message": "successfully constructed init file"}), 201

        def write_init(self,file_name):
            pinit = rpi.PencilInitResolver()
            pinit.set_init_json(self.data)
            configurable_file = pinit.build_file()
            with open("../../../"+str(file_name), "w") as file:
                file.write(configurable_file)
