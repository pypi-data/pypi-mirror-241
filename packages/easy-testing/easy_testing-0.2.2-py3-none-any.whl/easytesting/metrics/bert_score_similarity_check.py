from evaluate import load
from .metric import Metric
from ..test_case import SimilarityTestCase
from ..singleton import Singleton


class BertScoreSimilarityCheck(Metric, metaclass=Singleton):
    def __init__(self, minimum_score: float = 0.8):
        self.minimum_score = minimum_score
        self.bertscore = load("bertscore")

    def measure(self, test_case: SimilarityTestCase, *args, **kwargs):

        old_vs_reference = self.bertscore.compute(predictions=[test_case.old_text],
                                             references=[test_case.reference_text],
                                             lang=test_case.lang)[test_case.metric_to_use][0]
        new_vs_reference = self.bertscore.compute(predictions=[test_case.new_text],
                                             references=[test_case.reference_text],
                                             lang=test_case.lang)[test_case.metric_to_use][0]

        self.score = new_vs_reference / old_vs_reference
        self.success = self.score >= self.minimum_score

        return self.score

    def is_successful(self):
        return self.success

    @property
    def __name__(self):
        return "BertScoreSimilarityCheck"
