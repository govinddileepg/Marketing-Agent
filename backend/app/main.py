from fastapi import FastAPI
from .models import AnalyzeResponse, BusinessProfile
from .services import analyze_business, create_visibility_plan

app = FastAPI(title="Marketing Agent API", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "marketing-agent-api"}


@app.post("/api/v1/analyze", response_model=AnalyzeResponse)
def analyze(business: BusinessProfile) -> AnalyzeResponse:
    profile = analyze_business(business)
    plan = create_visibility_plan(business, profile)
    return AnalyzeResponse(business=business, marketing_profile=profile, visibility_plan=plan)
