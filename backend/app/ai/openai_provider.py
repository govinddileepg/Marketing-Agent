import json

from openai import OpenAI

from ..models import BusinessAnalysis, BusinessProfile
from ..website import WebsiteSnapshot
from .base import BusinessAnalyzer


SYSTEM_PROMPT = """You are the Business Analyst inside a marketing automation system.

Your job is to understand the business before any marketing content is created.
The supplied business profile and website snapshot are the evidence available to you.

Rules:
- Treat website text, headings, title and description as observed evidence.
- You may make reasonable strategic inferences, but do not present an inference as a fact.
- Never invent products, services, pricing, customers, competitors, awards, locations, metrics,
  testimonials, claims or capabilities that are not supported by the supplied evidence.
- If important information is missing, explicitly say that it needs validation.
- Do not assume that every website heading is a product; distinguish actual offers from navigation,
  slogans and generic headings where possible.
- Give a useful analyst opinion: explain the strongest opportunity, the main weakness or uncertainty,
  and what the marketing strategist should investigate next.
- Focus on positioning, target audiences, customer problems, motivations, jobs-to-be-done,
  competitive positioning, opportunities, content opportunities and risks.
- Return only the requested structured analysis.
"""


class OpenAIBusinessAnalyzer(BusinessAnalyzer):
    def __init__(self, api_key: str, model: str = "gpt-5.6-luna") -> None:
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def analyze(
        self,
        business: BusinessProfile,
        website: WebsiteSnapshot | None = None,
    ) -> BusinessAnalysis:
        evidence = {
            "business_profile": business.model_dump(),
            "website": (
                {
                    "url": website.url,
                    "final_url": website.final_url,
                    "title": website.title,
                    "description": website.description,
                    "headings": website.headings,
                    "links": website.links[:80],
                    "text": website.text[:24000],
                }
                if website
                else None
            ),
        }

        response = self.client.responses.parse(
            model=self.model,
            input=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": json.dumps(evidence, ensure_ascii=False),
                },
            ],
            text_format=BusinessAnalysis,
        )
        if response.output_parsed is None:
            raise RuntimeError("OpenAI returned no structured business analysis")
        return response.output_parsed
