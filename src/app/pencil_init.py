
from flask import request, jsonify
import resolvers.pencil_init as rpi

class PencilInit:
        def __init__(self, app):
            self.app = app
            self.data = None
            return


        def post_init(self, file_name):
            """
            posts a new .in file for tests
            at least a start.in run.in and print.in are required for testing
            :param file_name:
            :return:
            """

            self.data = request.get_json()

            try:
                pinit = rpi.PencilInitResolver()
                pinit.set_init_json(self.data)
                pinit.set_file_name(file_name)
                pinit.write_file()
            except:
                return jsonify({"message": "could not write start init file"}), 500

            return jsonify({"message": "successfully constructed start init file"}), 201



        def add_routes(self):
            self.app.add_url_rule('/init/:file_name', 'post_init', self.post_init, methods=["POST"])
