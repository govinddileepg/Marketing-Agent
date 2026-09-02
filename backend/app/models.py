from typing import List, Optional
from pydantic import BaseModel, Field


class BusinessProfile(BaseModel):
    name: str
    website: Optional[str] = None
    location: Optional[str] = None
    industry: str = "Unknown"
    description: str = ""
    target_customers: List[str] = Field(default_factory=list)
    products: List[str] = Field(default_factory=list)
    differentiators: List[str] = Field(default_factory=list)
    goals: List[str] = Field(default_factory=list)
    channels: List[str] = Field(default_factory=list)


class BusinessAnalysis(BaseModel):
    business_summary: str
    what_business_sells: List[str]
    target_audiences: List[str]
    customer_problems: List[str]
    customer_motivations: List[str]
    jobs_to_be_done: List[str]
    unique_value_proposition: str
    competitive_positioning: str
    brand_personality: List[str]
    strengths: List[str]
    weaknesses: List[str]
    market_opportunities: List[str]
    content_opportunities: List[str]
    recommended_positioning: str
    analyst_opinion: str


class MarketingProfile(BaseModel):
    positioning: str
    audience_segments: List[str]
    value_proposition: str
    content_pillars: List[str]
    recommended_channels: List[str]
    messaging_angles: List[str]
    opportunities: List[str]
    risks: List[str]


class VisibilityPlan(BaseModel):
    objective: str
    strategy: str
    content_mix: dict[str, int]
    weekly_focus: List[str]
    calls_to_action: List[str]
    success_metrics: List[str]


class AnalyzeResponse(BaseModel):
    business: BusinessProfile
    business_analysis: BusinessAnalysis
    marketing_profile: MarketingProfile
    visibility_plan: VisibilityPlan
