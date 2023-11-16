"""Asserting conceptual similarity
"""
from typing import Optional

from deepeval.singleton import Singleton
from deepeval.test_case import LLMTestCase
from deepeval.utils import cosine_similarity
from deepeval.evaluator import assert_test
from deepeval.progress_context import progress_context
from deepeval.metrics.base_metric import BaseMetric


class ConceptualSimilarityMetric(BaseMetric, metaclass=Singleton):
    """basic implementation of ConceptualSimilarityMetric"""

    def __init__(
        self,
        model_name: Optional[str] = "sentence-transformers/all-mpnet-base-v2",
        minimum_score: float = 0.7,
    ):
        from sentence_transformers import SentenceTransformer

        self.model_name = model_name
        with progress_context(
            "Downloading Conceptual Similarity model (may take up to 2 minutes if running for the first time)..."
        ):
            self.model = SentenceTransformer(self.model_name).eval()
        self.minimum_score = minimum_score

    def _vectorize(self, text_a: str, text_b: str):
        vectors = self.model.encode([text_a, text_b])
        return vectors

    def measure(self, test_case: LLMTestCase) -> float:
        if test_case.actual_output is None or test_case.expected_output is None:
            raise ValueError("Output or expected_output cannot be None")

        vectors = self._vectorize(
            test_case.actual_output, test_case.expected_output
        )
        self.score = cosine_similarity(vectors[0], vectors[1])
        self.success = self.score >= self.minimum_score
        return float(self.score)

    def is_successful(self) -> bool:
        return self.success

    @property
    def __name__(self):
        return "Conceptual Similarity"


def assert_conceptual_similarity(
    output: str, expected_output: str, minimum_score=0.7
):
    metric = ConceptualSimilarityMetric(minimum_score=minimum_score)
    test_case = LLMTestCase(
        input="placeholder",
        actual_output=output,
        expected_output=expected_output,
    )
    assert_test(test_case, [metric])


def is_conceptually_similar(
    output: str, expected_output: str, minimum_score=0.7
) -> bool:
    metric = ConceptualSimilarityMetric(minimum_score=minimum_score)
    test_case = LLMTestCase(
        input="placeholder",
        actual_output=output,
        expected_output=expected_output,
    )
    return metric.measure(test_case) >= minimum_score
