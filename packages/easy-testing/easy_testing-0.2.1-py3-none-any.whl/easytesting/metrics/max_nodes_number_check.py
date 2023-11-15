from .metric import Metric
from ..test_case import DeterministicTestCase
from ..singleton import Singleton


class MaxNodesCheck(Metric, metaclass=Singleton):
    def __init__(self, maximum_score: float = 1.15):
        self.maximum_score = maximum_score

    def measure(self, test_case: DeterministicTestCase, *args, **kwargs):
        self.score = test_case.output / test_case.input
        self.success = self.score <= self.maximum_score
        return self.score

    def is_successful(self):
        return self.success

    @property
    def __name__(self):
        return "MaxNodesNumberCheck"