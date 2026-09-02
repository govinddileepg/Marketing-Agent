import json

from openai import OpenAI

from ..models import BusinessAnalysis, BusinessProfile
from .base import BusinessAnalyzer


SYSTEM_PROMPT = """You are the Business Analyst inside a marketing automation system.
Analyze the supplied business facts and return practical, evidence-based marketing intelligence.
Do not invent products, claims, customers, competitors, locations, awards, or metrics that were not supplied.
If information is missing, make the uncertainty explicit rather than hallucinating facts.
Focus on positioning, customer needs, motivations, jobs-to-be-done, opportunities, content opportunities,
and risks that can be acted on by a downstream marketing strategist."""


class OpenAIBusinessAnalyzer(BusinessAnalyzer):
    def __init__(self, api_key: str, model: str = "gpt-5.6-luna") -> None:
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def analyze(self, business: BusinessProfile) -> BusinessAnalysis:
        response = self.client.responses.parse(
            model=self.model,
            input=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": json.dumps(business.model_dump(), ensure_ascii=False),
                },
            ],
            text_format=BusinessAnalysis,
        )
        if response.output_parsed is None:
            raise RuntimeError("OpenAI returned no structured business analysis")
        return response.output_parsed
