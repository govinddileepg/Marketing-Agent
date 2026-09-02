from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from .models import AnalyzeResponse, BusinessProfile
from .services import analyze_business, create_visibility_plan, understand_business
from .website import fetch_website

app = FastAPI(title="Marketing Agent API", version="0.2.0")


class WebsiteAnalyzeRequest(BaseModel):
    website: str
    business: BusinessProfile | None = None


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "marketing-agent-api"}


@app.post("/api/v1/analyze", response_model=AnalyzeResponse)
def analyze(business: BusinessProfile) -> AnalyzeResponse:
    profile = analyze_business(business)
    plan = create_visibility_plan(business, profile)
    analysis = understand_business(business)
    return AnalyzeResponse(
        business=business,
        business_analysis=analysis,
        marketing_profile=profile,
        visibility_plan=plan,
    )


@app.post("/api/v1/analyze/website", response_model=AnalyzeResponse)
def analyze_website(request: WebsiteAnalyzeRequest) -> AnalyzeResponse:
    try:
        website = fetch_website(request.website)
    except Exception as exc:
        raise HTTPException(status_code=422, detail=f"Unable to read website: {exc}") from exc

    business = request.business or BusinessProfile(
        name=website.title or request.website,
        website=website.final_url,
        description=website.description,
        industry="To be classified from website research",
    )
    business.website = website.final_url
    if not business.description:
        business.description = website.description

    analysis = understand_business(business, website)
    profile = analyze_business(business)
    plan = create_visibility_plan(business, profile)
    return AnalyzeResponse(
        business=business,
        business_analysis=analysis,
        marketing_profile=profile,
        visibility_plan=plan,
    )
