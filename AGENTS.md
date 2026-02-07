# AGENTS

## Purpose
This repository is a modular e-commerce backend. Agents should keep changes minimal, predictable, and aligned with the clean architecture layout under `app/`.

## Operating Principles
- Prefer small, composable services and interfaces.
- Keep domain models in `app/core/models` and avoid framework-specific imports in domain code.
- Add new API routes under `app/api/routes` and include them in `app/main.py`.
- For any new dependency, update `requirements.txt` and explain why in the PR message.
- Use dependency injection via interfaces in `app/core/interfaces`.

## Code Style
- Python 3.11+
- Prefer `dataclasses` for domain models.
- Add type hints to new code.
- Keep functions under ~50 lines where reasonable.

## Testing
- If you add business logic, add or update tests (create `tests/` if needed).
- Prefer unit tests around services and filter logic.

## Repository Conventions
- `app/` holds all application code.
- `docs/` holds architecture, roadmap, and operational notes.
- `app/db/migrations` is reserved for DB migration tools (Alembic or equivalent).

## Safety
- Do not remove unrelated files.
- Avoid large refactors unless requested.
