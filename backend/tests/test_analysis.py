from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def sample_business() -> dict:
    return {
        "name": "Example Business",
        "industry": "Wedding services",
        "description": "A business offering custom wedding products.",
        "target_customers": ["Engaged couples"],
        "products": ["Custom wedding invitations"],
        "differentiators": ["Personalized design"],
        "goals": ["Increase enquiries"],
        "channels": ["Instagram"],
    }


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_analysis_uses_mock_provider_by_default(monkeypatch) -> None:
    monkeypatch.setenv("AI_PROVIDER", "mock")
    response = client.post("/api/v1/analyze", json=sample_business())

    assert response.status_code == 200
    body = response.json()
    assert body["analysis"]["target_audience"] == ["Engaged couples"]
    assert body["marketing_profile"]["recommended_channels"] == ["Instagram"]
    assert body["visibility_plan"]["objective"]
