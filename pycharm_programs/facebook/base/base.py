import json
import yaml

class Base(object):
    ''' Base level methods '''

    def __init__(self):
        pass

    def read_app_data(self, data_file):
        ''' Reads information from JSON/YAML file and returns a dictionary '''

        if data_file.endswith('.json'):
            test_data = json.loads(data_file)
        if data_file.endswith('.yaml'):
            test_data = yaml.safe_load(data_file)

        return test_data
