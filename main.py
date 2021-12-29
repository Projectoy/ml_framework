from arguments_setting import ArgumentManager

class Main:
    def __init__(self):
        model_list = self.load_model_list()
        self.arg_mngr = ArgumentManager(model_list = model_list)
        self.config_path = self.arg_mngr.get_configuraiton_file_path()
        self.model_type = self.arg_mngr.get_model_type()
        self.task_type = self.arg_mngr.get_task_type()
        self.print_initialized_main()

    def print_initialized_main(self):
        print("configuration path:{0}".format(self.config_path))
        print("model_type:{0}".format(self.model_type))
        print("task_type:{0}".format(self.task_type))

    def load_model_list(self):
        path = "./list_of_models.txt"
        list = []
        with open(path, "r") as fp:
            for line in fp:
                line = line.strip()
                list.append(line)
        return list

if __name__ == '__main__':
    main = Main()
