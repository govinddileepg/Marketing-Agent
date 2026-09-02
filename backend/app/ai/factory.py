import os

from .base import BusinessAnalyzer
from .mock import MockBusinessAnalyzer


def get_business_analyzer() -> BusinessAnalyzer:
    provider = os.getenv("AI_PROVIDER", "mock").lower()

    if provider == "openai":
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("AI_PROVIDER=openai requires OPENAI_API_KEY")
        from .openai_provider import OpenAIBusinessAnalyzer

        return OpenAIBusinessAnalyzer(
            api_key=api_key,
            model=os.getenv("OPENAI_MODEL", "gpt-5.6-luna"),
        )

    if provider == "mock":
        return MockBusinessAnalyzer()

    raise ValueError(f"Unsupported AI_PROVIDER: {provider}")
