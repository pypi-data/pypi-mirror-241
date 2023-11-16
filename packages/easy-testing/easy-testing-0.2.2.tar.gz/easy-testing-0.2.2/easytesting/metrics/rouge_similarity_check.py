from evaluate import load
from .metric import Metric
from ..test_case import SimilarityTestCase
from ..singleton import Singleton


class RougeSimilarityCheck(Metric, metaclass=Singleton):
    def __init__(self, minimum_score: float = 0.8):
        self.maximum_score = minimum_score

    def measure(self, test_case: SimilarityTestCase, *args, **kwargs):
        rouge = load("rouge")

        old_vs_reference = rouge.compute(predictions=[test_case.old_text],
                                         references=[test_case.reference_text],
                                         use_aggregator=False)[test_case.metric_to_use][0]
        new_vs_reference = rouge.compute(predictions=[test_case.new_text],
                                         references=[test_case.reference_text],
                                         use_aggregator=False)[test_case.metric_to_use][0]

        self.score = new_vs_reference / old_vs_reference
        self.success = self.score >= self.maximum_score

        return self.score

    def is_successful(self):
        return self.success

    @property
    def __name__(self):
        return "RougeSimilarityCheck"
