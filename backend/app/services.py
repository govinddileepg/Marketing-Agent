from .ai.factory import get_business_analyzer
from .models import BusinessAnalysis, BusinessProfile, MarketingProfile, VisibilityPlan


def analyze_business_with_ai(business: BusinessProfile) -> BusinessAnalysis:
    """Run the configured business-analysis provider."""
    return get_business_analyzer().analyze(business)


def build_marketing_profile(business: BusinessProfile, analysis: BusinessAnalysis) -> MarketingProfile:
    return MarketingProfile(
        positioning=analysis.recommended_positioning,
        audience_segments=analysis.target_audience,
        value_proposition=analysis.business_summary,
        content_pillars=(
            analysis.content_opportunities[:5]
            or ["Product showcase", "Education and inspiration", "Trust and social proof"]
        ),
        recommended_channels=business.channels or ["Instagram", "Facebook"],
        messaging_angles=analysis.unique_selling_propositions[:5] + analysis.customer_motivations[:3],
        opportunities=analysis.market_opportunities,
        risks=analysis.weaknesses_and_risks,
    )


def create_visibility_plan(business: BusinessProfile, profile: MarketingProfile) -> VisibilityPlan:
    return VisibilityPlan(
        objective="Increase qualified visibility and convert attention into enquiries.",
        strategy=(
            "Use a repeatable mix of product-led visuals, useful/inspirational content, "
            "trust-building proof and conversion-focused posts. Adapt the message to each platform."
        ),
        content_mix={
            "product_showcase": 30,
            "education_inspiration": 25,
            "trust_proof": 20,
            "behind_scenes": 15,
            "conversion": 10,
        },
        weekly_focus=[
            "Week 1: Establish positioning and visual identity",
            "Week 2: Demonstrate products and use cases",
            "Week 3: Build trust with proof and process",
            "Week 4: Push enquiries with strong offers and CTAs",
        ],
        calls_to_action=[
            "DM for details",
            "Visit the website",
            "Request a quote",
            "Save this post",
            "Share with someone who needs this",
        ],
        success_metrics=[
            "Reach",
            "Profile visits",
            "Website clicks",
            "Saves/shares",
            "Qualified enquiries",
            "Conversion to orders",
        ],
    )
