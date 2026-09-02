from .models import BusinessAnalysis, BusinessProfile, MarketingProfile, VisibilityPlan
from .website import WebsiteSnapshot


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


def understand_business(business: BusinessProfile, website: WebsiteSnapshot | None = None) -> BusinessAnalysis:
    site_text = website.text if website else ""
    site_title = website.title if website else ""
    site_description = website.description if website else ""
    headings = website.headings if website else []

    summary = business.description or site_description or f"{business.name} operates in the {business.industry} space."
    products = business.products or ([h for h in headings if len(h) < 120][:8] or ["Core products/services"])
    audiences = business.target_customers or ["Visitors and potential customers identified from the business proposition"]
    problems = [
        "Customers need to understand the value and relevance of the offering quickly",
        "Customers need confidence before making an enquiry or purchase",
    ]
    motivations = ["Convenience", "Quality", "Trust", "A clear outcome"]
    jobs = ["Discover a suitable solution", "Compare options", "Make a confident purchase decision"]

    if site_description:
        summary = site_description
    if site_title and site_title.lower() not in summary.lower():
        summary = f"{site_title}. {summary}"

    evidence_note = "Website content was supplied to the analyst." if website else "No website content was supplied; conclusions are based on the provided business profile."
    text_signal = site_text[:400].replace("\n", " ") if site_text else "No website text was available."

    return BusinessAnalysis(
        business_summary=f"{summary} {evidence_note}",
        what_business_sells=products,
        target_audiences=audiences,
        customer_problems=problems,
        customer_motivations=motivations,
        jobs_to_be_done=jobs,
        unique_value_proposition=(
            business.differentiators[0] if business.differentiators else
            "The strongest value proposition needs to be validated from the business's actual offer and customer proof."
        ),
        competitive_positioning=(
            f"Position {business.name} around a specific customer outcome rather than competing only on features. "
            "The next research step should benchmark direct competitors and pricing."
        ),
        brand_personality=["Clear", "Trustworthy", "Customer-focused", "Visually consistent"],
        strengths=[
            "The business can turn its real products/services into concrete marketing assets",
            "A focused value proposition can be repeated consistently across channels",
            f"Website messaging provides initial market signals: {text_signal}",
        ],
        weaknesses=[
            "Competitor and market data has not yet been independently benchmarked",
            "Customer proof, reviews and conversion performance are not yet connected",
            "The current analysis should not infer claims that are not supported by source evidence",
        ],
        market_opportunities=[
            "Own a clearly defined customer problem and occasion",
            "Create differentiated content around real products and customer outcomes",
            "Build trust through examples, reviews and demonstrations",
        ],
        content_opportunities=[
            "Product/service showcases",
            "Before-and-after or process demonstrations",
            "Customer questions and educational posts",
            "Social proof and customer stories",
            "Strong conversion-focused offers",
        ],
        recommended_positioning=(
            f"Make {business.name} easy to understand in seconds: who it is for, what it offers, "
            "why it is different, and what the customer should do next."
        ),
        analyst_opinion=(
            "The business is understandable at a high level, but a confident strategic opinion requires "
            "competitor, audience and performance evidence in addition to website copy."
        ),
    )


def create_visibility_plan(business: BusinessProfile, profile: MarketingProfile) -> VisibilityPlan:
    return VisibilityPlan(
        objective="Increase qualified visibility and convert attention into enquiries.",
        strategy=(
            "Use a repeatable mix of product-led visuals, useful/inspirational content, trust-building proof "
            "and conversion-focused posts. Adapt the message to each platform."
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
