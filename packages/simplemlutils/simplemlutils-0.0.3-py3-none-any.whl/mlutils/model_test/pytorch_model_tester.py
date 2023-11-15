from abc import abstractmethod
from .model_performance import ClassifierPerformance


class PyTorchModelTester(object):
    def __init__(self, model):
        self.model = model

    @abstractmethod
    def run(self):
        pass


class PyTorchClassifierModelTester(PyTorchModelTester):
    def __init__(self, model):
        super(PyTorchClassifierModelTester, self).__init__(model)

    def run(self) -> ClassifierPerformance:
        return None
