from configuration import Configuration

class ConfigurationForBERT(Configuration):
    def __init__(self, config_file_path):
        super().__init__(config_file_path)

    def validate_configuration_values(self):
        if self.dict == None:
            raise ReferenceError


if __name__ == "__main__":
    path = "/Users/jeonghoon/PycharmProjects/learning_framework/configuration/config_json_file/config_bert.json"
    config = ConfigurationForBERT(path)
    print("a")