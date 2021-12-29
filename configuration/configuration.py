import os
import json


class Configuration:

    def __init__(self, configuration_file_path):
        self.dict = None
        if not self.check_file_exists(configuration_file_path):
            raise FileNotFoundError
        self.path = configuration_file_path
        self.dict = self.load_configuration_json(self.path)

    def check_file_exists(selfl, file_path):
        return (os.path.exists(file_path) and os.path.isfile(file_path))

    def load_configuration_json(self, file_path):
        json_data = None
        with open(file_path) as fp:
            try:
                json_data = json.load(fp)
            except:
                assert False, "check the json file: {0}".format(file_path)
        return json_data