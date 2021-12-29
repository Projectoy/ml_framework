import argparse, os

class ArgumentManager:
    def __init__(self, model_list):
        self.model_list = model_list
        self.args = self.get_input_arguments()
        self.validate_arguments()

    def get_input_arguments(self):
        parser = argparse.ArgumentParser(description='Process some integers.')
        parser.add_argument("--configuration", "-c", required=True, help="the path of a configuration file(json type)")
        parser.add_argument("--model", "-m", required=True, help="the model to process")
        parser.add_argument("--task", "-t",  required=True, help="training/testing")
        return parser.parse_args()

    def validate_arguments(self):
        self.validate_configuration_path()
        self.validate_model()
        self.validate_task()

    def validate_task(self):
        task = self.args.task
        assert task == "training" or task == "testing", "task should be training or testing"

    def validate_model(self):
        model = self.args.model
        assert model in self.model_list, "model is not in the prepared model list"

    def validate_configuration_path(self):
        config_path = self.args.configuration
        assert os.path.exists(config_path), "configuration path is inappropriate (not found file)"

    def get_configuraiton_file_path(self):
        return self.args.configuration

    def get_model_type(self):
        return self.args.model

    def get_task_type(self):
        return self.args.task