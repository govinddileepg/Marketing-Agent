from ..models import BusinessAnalysis, BusinessProfile
from .base import BusinessAnalyzer


class MockBusinessAnalyzer(BusinessAnalyzer):
    """Deterministic fallback used when no AI provider is configured."""

    def analyze(self, business: BusinessProfile) -> BusinessAnalysis:
        audience = business.target_customers or ["Potential customers"]
        products = business.products or ["Core products/services"]
        differentiators = business.differentiators or ["Quality and customer experience"]

        return BusinessAnalysis(
            business_summary=(
                f"{business.name} is a {business.industry} business focused on "
                f"{products[0].lower()}."
            ),
            target_audience=audience,
            customer_pain_points=[
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
            unique_selling_propositions=differentiators,
            competitive_positioning=(
                f"Position {business.name} around its strongest differentiator: "
                f"{differentiators[0].lower()}, rather than competing only on price."
            ),
            brand_personality=["Trustworthy", "Clear", "Helpful", "Consistent"],
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
            weaknesses_and_risks=[
                "Generic content can weaken differentiation",
                "Inconsistent visuals can reduce brand recognition",
                "Claims without evidence can reduce trust",
            ],
            recommended_positioning=(
                f"{business.name}: a {business.industry} brand that helps {audience[0].lower()} "
                f"choose {products[0].lower()} with confidence."
            ),
        )
