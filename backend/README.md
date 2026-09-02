# Marketing Agent API

FastAPI service for the first vertical: business analysis and visibility strategy.

## Run locally

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Health check: `GET /health`

Analysis endpoint: `POST /api/v1/analyze`

The current implementation is deterministic scaffolding. AI provider integration will be added behind the same service boundary so the API contract remains stable.
