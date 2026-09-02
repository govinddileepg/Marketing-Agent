import os

from .base import BusinessAnalyzer
from .mock import MockBusinessAnalyzer


def get_business_analyzer() -> BusinessAnalyzer:
    provider = os.getenv("AI_PROVIDER", "mock").lower()

    if provider in {"openrouter", "openai"}:
        if provider == "openrouter":
            api_key = os.getenv("OPENROUTER_API_KEY")
            if not api_key:
                raise RuntimeError("AI_PROVIDER=openrouter requires OPENROUTER_API_KEY")
            from .openai_provider import OpenAIBusinessAnalyzer

            return OpenAIBusinessAnalyzer(
                api_key=api_key,
                model=os.getenv("OPENROUTER_MODEL", "openrouter/free"),
                base_url="https://openrouter.ai/api/v1",
                app_url=os.getenv("NEXT_PUBLIC_APP_URL"),
                app_name="Marketing Agent",
            )

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
