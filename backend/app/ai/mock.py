from ..models import BusinessAnalysis, BusinessProfile
from ..website import WebsiteSnapshot
from .base import BusinessAnalyzer


class MockBusinessAnalyzer(BusinessAnalyzer):
    """Deterministic fallback used when no AI provider is configured."""

    def analyze(
        self,
        business: BusinessProfile,
        website: WebsiteSnapshot | None = None,
    ) -> BusinessAnalysis:
        audience = business.target_customers or ["Potential customers"]
        products = business.products or ["Core products/services"]
        differentiators = business.differentiators or ["Quality and customer experience"]

        return BusinessAnalysis(
            business_summary=(
                f"{business.name} is a {business.industry} business focused on "
                f"{products[0].lower()}."
            ),
            what_business_sells=products,
            target_audiences=audience,
            customer_problems=[
                "Difficulty comparing suitable options",
                "Uncertainty about quality and value",
                "Friction between discovering a product and making an enquiry",
            ],
            customer_motivations=[
                "Confidence that they are making the right choice",
                "A convenient buying or enquiry experience",
                "Visible quality and proof from real examples",
            ],
            jobs_to_be_done=[
                f"Find and evaluate {products[0].lower()}",
                "Understand why this business is different",
                "Move from interest to enquiry with minimal friction",
            ],
            unique_value_proposition=differentiators[0],
            competitive_positioning=(
                f"Position {business.name} around its strongest differentiator: "
                f"{differentiators[0].lower()}, rather than competing only on price."
            ),
            brand_personality=["Trustworthy", "Clear", "Helpful", "Consistent"],
            strengths=[
                "Real products/services can be turned into concrete marketing assets",
                "A focused value proposition can be repeated consistently",
            ],
            weaknesses=[
                "Competitor and market data has not been benchmarked",
                "Customer proof and conversion performance are not connected",
                "Website evidence is not available to the mock provider as reasoning input",
            ],
            market_opportunities=[
                "Turn existing products and customer outcomes into recurring content",
                "Own specific audience use cases instead of broad generic messaging",
                "Build local and occasion-specific relevance where appropriate",
            ],
            content_opportunities=[
                "Product demonstrations",
                "Educational and inspirational posts",
                "Customer proof and testimonials",
                "Behind-the-scenes process content",
                "Offer and enquiry-focused content",
            ],
            recommended_positioning=(
                f"{business.name}: a {business.industry} brand that helps {audience[0].lower()} "
                f"choose {products[0].lower()} with confidence."
            ),
            analyst_opinion=(
                "This is a deterministic fallback. Switch AI_PROVIDER to openai for evidence-based "
                "analysis of the supplied website and business information."
            ),
        )
