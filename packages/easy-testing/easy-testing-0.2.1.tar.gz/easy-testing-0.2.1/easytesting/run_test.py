from dataclasses import dataclass
from typing import List, Optional, Union
import time
from .test_case import TestCase, DeterministicTestCase, SimilarityTestCase
from .metrics import Metric


class TestError(Exception):
    def __init__(self, message, code, score, metric):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)

        # Now for your custom code...
        self.message = message
        self.code = code
        self.score = score
        self.metric = metric


@dataclass
class TestResult:
    """Returned from run_test
    represents the results of a test conducted by the run_test function
    """

    success: bool
    score: float
    metric_name: str
    output: float = 0
    input: float = 0
    new_text: str = "-"
    old_text: str = "-"
    reference_text: str = "-"
    lang: str = "it"
    metric_to_use: Optional[str] = None

    #two methods for comparison of the score attribute: grater-than and less-than
    def __gt__(self, other: "TestResult") -> bool:
        """Greater than comparison based on score"""
        return self.score > other.score

    def __lt__(self, other: "TestResult") -> bool:
        """Less than comparison based on score"""
        return self.score < other.score


def create_test_result(
    test_case: Union[DeterministicTestCase],
    success: bool,
    score: float,
    metric: float,
) -> TestResult:
    if isinstance(test_case, DeterministicTestCase):
        return TestResult(
            success=success,
            score=score,
            metric_name=metric.__name__,
            input=test_case.input if test_case.input else 0,
            output=test_case.output if test_case.output else 0,
        )
    elif isinstance(test_case, SimilarityTestCase):
        return TestResult(
            success=success,
            score=score,
            metric_name=metric.__name__,
            reference_text=test_case.reference_text if test_case.reference_text else "-",
            old_text=test_case.old_text if test_case.old_text else "-",
            new_text=test_case.new_text if test_case.new_text else "-",
            lang=test_case.lang if test_case.lang else "-",
            metric_to_use=test_case.metric_to_use if test_case.metric_to_use else "-",
        )
    else:
        raise ValueError("TestCase not supported yet.")


def run_test(
    test_cases: Union[TestCase, DeterministicTestCase],
    metrics: List[Metric],
    #cambiare parametri retry
    #max_retries: int = 1,
    #delay: int = 1,
    #min_success: int = 1,
    raise_error: bool = False,
) -> List[TestResult]:
    """
    Args:
        test_cases: Either a single test case or a list of test cases to run
        metrics: List of metrics to run
        raise_error: Whether to raise an error if a metric fails
        max_retries: Maximum number of retries for each metric measurement
        delay: Delay in seconds between retries
        min_success: Minimum number of successful measurements required

    """
    if isinstance(test_cases, TestCase):
        test_cases = [test_cases]

        test_results = []
        for test_case in test_cases:
            failed_metrics = []
            for metric in metrics:
                test_start_time = time.perf_counter()

                #add @retry
                def measure_metric():
                    score = metric.measure(test_case)
                    success = metric.is_successful()
                    test_result = create_test_result(test_case, success, score, metric)
                    test_results.append(test_result)

                    # Load the test_run and add the test_case regardless of the success of the test
                    test_end_time = time.perf_counter()
                    run_duration = test_end_time - test_start_time
                    # if os.getenv(PYTEST_RUN_ENV_VAR): ???
                    #     test_run = TestRun.load()
                    #     metric.score = score
                    #     test_run.add_llm_test_case(
                    #         test_case=test_case,
                    #         metrics=[metric],
                    #         run_duration=run_duration,
                    #     )
                    #     test_run.save()

                    if not success:
                        failed_metrics.append((metric.__name__, score))

                measure_metric()

        if raise_error and failed_metrics:
            raise TestError(message=f"Metrics {', '.join([f'{name} (Score: {score})' for name, score in failed_metrics])} failed.",
                            code=525,
                            score = f"{', '.join([f'{score}' for name, score in failed_metrics])}",
                            metric = f"{', '.join([f'{name}' for name, score in failed_metrics])}")

        return test_results


def assert_test(
    test_cases: Union[DeterministicTestCase, List[DeterministicTestCase]],
    metrics: List[Metric],
    # max_retries: int = 1,
    # delay: int = 1,
    # min_success: int = 1,
) -> List[TestResult]:
    """Assert a test"""
    return run_test(
        test_cases=test_cases,
        metrics=metrics,
        #max_retries=max_retries,
        #delay=delay,
        #min_success=min_success,
        raise_error=True,
    )