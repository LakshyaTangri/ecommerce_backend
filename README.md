# E-Commerce Backend (Python OOP)

This is a scaffold for a modular e-commerce backend API.

## Quick start

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Structure

- `app/api` REST API routes and serializers
- `app/core` Domain models, interfaces, services
- `app/scraper` Scraping base, sources, scheduler
- `app/categorization` Categorization and filtering
- `app/analytics` Analytics services and reports
- `app/db` Repositories and migrations

## Notes
- This is a scaffold. Replace in-memory repos with real DB implementations.
- Extend services and routes as you implement features.
