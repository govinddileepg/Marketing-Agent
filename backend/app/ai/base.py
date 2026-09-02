from abc import ABC, abstractmethod

from ..models import BusinessAnalysis, BusinessProfile
from ..website import WebsiteSnapshot


class BusinessAnalyzer(ABC):
    """Provider-neutral interface for business analysis."""

    @abstractmethod
    def analyze(
        self,
        business: BusinessProfile,
        website: WebsiteSnapshot | None = None,
    ) -> BusinessAnalysis:
        raise NotImplementedError
