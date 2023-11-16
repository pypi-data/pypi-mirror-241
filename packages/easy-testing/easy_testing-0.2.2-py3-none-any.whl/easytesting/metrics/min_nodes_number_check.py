from .metric import Metric
from ..test_case import DeterministicTestCase
from ..singleton import Singleton


class MinNodesCheck(Metric, metaclass=Singleton):
    def __init__(self, minimum_score: float = 0.85):
        self.minimum_score = minimum_score

    def measure(self, test_case: DeterministicTestCase, *args, **kwargs):
        self.score = test_case.output / test_case.input
        self.success = self.score >= self.minimum_score
        return self.score

    def is_successful(self):
        return self.success

    @property
    def __name__(self):
        return "MinNodesNumberCheck"