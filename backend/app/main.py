from fastapi import FastAPI

from .models import AnalyzeResponse, BusinessProfile
from .services import analyze_business_with_ai, build_marketing_profile, create_visibility_plan

app = FastAPI(title="Marketing Agent API", version="0.2.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "marketing-agent-api"}


@app.post("/api/v1/analyze", response_model=AnalyzeResponse)
def analyze(business: BusinessProfile) -> AnalyzeResponse:
    analysis = analyze_business_with_ai(business)
    profile = build_marketing_profile(business, analysis)
    plan = create_visibility_plan(business, profile)
    return AnalyzeResponse(
        business=business,
        analysis=analysis,
        marketing_profile=profile,
        visibility_plan=plan,
    )
