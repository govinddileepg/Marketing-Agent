# Marketing Agent

AI-powered marketing automation platform that turns business context and real product assets into a measurable social-media marketing workflow.

## V1 goal

**Analyse → Strategise → Plan → Create → Approve → Publish**

The first test business is Invitepedia. The existing Invite Studio repository is intentionally separate and will not be modified by this project.

## Architecture

```text
Business onboarding
      ↓
Business Analyst
      ↓
Marketing Profile
      ↓
Marketing Strategist
      ↓
Visibility Plan
      ↓
Content Planner
      ↓
Creative Generator
      ↓
QA / Human Approval
      ↓
Social Publisher
      ↓
Analytics
      ↓
Optimization
```

## Initial principles

- Keep business knowledge structured and reusable.
- Use real business/product assets instead of inventing products.
- Separate AI providers behind provider interfaces.
- Keep image/video providers replaceable.
- Require human approval before public publishing in V1.
- Treat publishing as a validated workflow, not an LLM free-form action.
- Build toward analytics-driven optimization and eventual autopilot.

## Planned stack

- Next.js + TypeScript for the web application
- FastAPI/Python for AI and workflow services where useful
- PostgreSQL/Supabase for persistence
- Object storage for business/product assets
- OpenAI and Anthropic provider abstraction
- Image/video provider abstraction
- SocialClaw for social publishing
- Background job/workflow layer for generation and publishing

## Repository boundary

This repository is the new Marketing Agent product. **Do not modify `govinddileepg/Invite-Studio` as part of this project.**

## Development status

Phase 0 — repository foundation.
