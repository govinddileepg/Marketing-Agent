from abc import ABC, abstractmethod

from ..models import BusinessAnalysis, BusinessProfile


class BusinessAnalyzer(ABC):
    """Provider-neutral interface for business analysis."""

    @abstractmethod
    def analyze(self, business: BusinessProfile) -> BusinessAnalysis:
        raise NotImplementedError
