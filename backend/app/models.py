from typing import List, Optional
from pydantic import BaseModel, Field


class BusinessProfile(BaseModel):
    name: str
    website: Optional[str] = None
    location: Optional[str] = None
    industry: str
    description: str
    target_customers: List[str] = Field(default_factory=list)
    products: List[str] = Field(default_factory=list)
    differentiators: List[str] = Field(default_factory=list)
    goals: List[str] = Field(default_factory=list)
    channels: List[str] = Field(default_factory=list)


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
    marketing_profile: MarketingProfile
    visibility_plan: VisibilityPlan
