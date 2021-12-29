

class TaskLearning:

    def __init__(self):
        pass
        ### setting
        # configuration
        # model
        # optimizer

    def start_learning(self):
        epoch = 10

        self.callback_before_starting()
        for _ in range(epoch):
            iterations = 1000
            self.callback_before_each_epoch()
            for cur_iter in range(iterations):
                self.callback_before_each_iteration()
                # todo - forward and backward passes
                self.callback_after_each_iteration()
            self.callback_after_each_epoch()
        self.callback_after_finishing()

    def callback_before_starting(self):
        pass

    def callback_before_each_epoch(self):
        pass

    def callback_before_each_iteration(self):
        pass

    def callback_after_each_iteration(self):
        pass

    def callback_after_each_epoch(self):
        pass

    def callback_after_finishing(self):
        pass

    def print_iteration_info(self):
        pass

    def print_epoch_info(self):
        pass

    def print_validation_info(self):
        pass

