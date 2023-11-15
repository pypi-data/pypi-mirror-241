"""Investigate test case.
"""
import hashlib
from dataclasses import dataclass
from typing import Any, List, Optional, Union


@dataclass
class TestCase:
    id: Optional[str] = None

    def __post_init__(self):
        """it checks if id is None. If it is, it generates a unique id for the test case based on a hash of the values of all attributes.
        This ensures that each TestCase instance has a unique identifier."""
        if self.id is None:
            id_string = "".join(str(value) for value in self.__dict__.values())
            self.id = hashlib.md5(id_string.encode()).hexdigest()

@dataclass
class DeterministicTestCase(TestCase):
    type: str = "-"
    input: float = 0
    output: float = 0

    def __post_init__(self):
        super().__post_init__()
        self.__name__ = f"DeterministicTestCase_{self.id}"

@dataclass
class SimilarityTestCase(TestCase):
    type: str = "-"
    new_text: str = "-"
    old_text: str = "-"
    reference_text: str = "-"
    lang: str = "it"
    metric_to_use: str = "f1"  # Allowed options for bertScore: "f1", "precision", "recall" - for rouge: "rouge1", "rouge2", "rougeL", "rougeLsum"

    def __post_init__(self):
        super().__post_init__()
        self.__name__ = f"SimilarityTestCase_{self.id}"
