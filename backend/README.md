# Marketing Agent API

FastAPI backend for the first vertical: business analysis and visibility strategy.

## Current pipeline

`BusinessProfile -> Business Analysis -> Marketing Profile -> Visibility Plan`

The `/api/v1/analyze` endpoint uses a provider abstraction. It defaults to a deterministic `mock` provider so development does not require API credentials. Set `AI_PROVIDER=openai` and `OPENAI_API_KEY` to use OpenAI structured output.

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

## Example configuration

```env
AI_PROVIDER=openai
OPENAI_API_KEY=your-key
OPENAI_MODEL=gpt-5.6-luna
```

The AI layer is isolated from business logic so additional providers can be added without changing the API contract.
