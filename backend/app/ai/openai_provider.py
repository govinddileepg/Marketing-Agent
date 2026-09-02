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
    """Business analyzer using an OpenAI-compatible API endpoint."""

    def __init__(
        self,
        api_key: str,
        model: str = "gpt-5.6-luna",
        base_url: str | None = None,
        app_url: str | None = None,
        app_name: str = "Marketing Agent",
    ) -> None:
        kwargs = {"api_key": api_key}
        if base_url:
            kwargs["base_url"] = base_url
        self.client = OpenAI(**kwargs)
        self.model = model
        self.app_url = app_url
        self.app_name = app_name

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

        extra_headers = {}
        if self.app_url:
            extra_headers["HTTP-Referer"] = self.app_url
        if self.app_name:
            extra_headers["X-OpenRouter-Title"] = self.app_name

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": json.dumps(evidence, ensure_ascii=False),
                },
            ],
            response_format={"type": "json_object"},
            extra_headers=extra_headers or None,
        )

        content = response.choices[0].message.content
        if not content:
            raise RuntimeError("AI provider returned no business analysis")

        try:
            return BusinessAnalysis.model_validate_json(content)
        except Exception as exc:
            raise RuntimeError("AI provider returned invalid business-analysis JSON") from exc
