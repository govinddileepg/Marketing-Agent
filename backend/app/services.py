from .models import BusinessProfile, MarketingProfile, VisibilityPlan


def analyze_business(business: BusinessProfile) -> MarketingProfile:
    audience = business.target_customers or ["Potential customers"]
    products = business.products or ["Core products/services"]
    differentiators = business.differentiators or ["Product quality and customer experience"]

    return MarketingProfile(
        positioning=(
            f"{business.name} should be positioned as a {business.industry} brand that makes "
            f"{products[0].lower()} easier to discover and choose, with emphasis on "
            f"{differentiators[0].lower()}."
        ),
        audience_segments=audience,
        value_proposition=(
            f"Help {audience[0].lower()} understand the value of {products[0].lower()} "
            f"and move from discovery to enquiry with less friction."
        ),
        content_pillars=[
            "Product showcase", "Education and inspiration", "Trust and social proof",
            "Behind the scenes", "Offers and conversion",
        ],
        recommended_channels=business.channels or ["Instagram", "Facebook"],
        messaging_angles=[
            "Show the product in a real customer context",
            "Explain why the product is worth choosing",
            "Demonstrate quality and attention to detail",
            "Use proof, examples and customer outcomes",
            "Create a clear path from post to enquiry",
        ],
        opportunities=[
            "Turn existing products into recurring visual content",
            "Build recognizable content pillars instead of isolated posts",
            "Use local audience and occasion-specific messaging",
        ],
        risks=[
            "Generic AI-generated content can dilute brand identity",
            "Inconsistent visual style can reduce recognition",
            "Publishing without approval can create brand-safety issues",
        ],
    )


def create_visibility_plan(business: BusinessProfile, profile: MarketingProfile) -> VisibilityPlan:
    return VisibilityPlan(
        objective="Increase qualified visibility and convert attention into enquiries.",
        strategy=(
            "Use a repeatable mix of product-led visuals, useful/inspirational content, "
            "trust-building proof and conversion-focused posts. Adapt the message to each platform."
        ),
        content_mix={"product_showcase": 30, "education_inspiration": 25, "trust_proof": 20, "behind_scenes": 15, "conversion": 10},
        weekly_focus=[
            "Week 1: Establish positioning and visual identity",
            "Week 2: Demonstrate products and use cases",
            "Week 3: Build trust with proof and process",
            "Week 4: Push enquiries with strong offers and CTAs",
        ],
        calls_to_action=["DM for details", "Visit the website", "Request a quote", "Save this post", "Share with someone who needs this"],
        success_metrics=["Reach", "Profile visits", "Website clicks", "Saves/shares", "Qualified enquiries", "Conversion to orders"],
    )
