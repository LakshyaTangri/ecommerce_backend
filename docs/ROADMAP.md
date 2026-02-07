# Roadmap

## Milestone 1: Baseline API and domain (2 weeks)
- Create core domain models and interfaces
- Build in-memory repositories and services
- Add health check and basic product endpoints
- Document API contract and filters

## Milestone 2: Data persistence and auth (3 weeks)
- Integrate PostgreSQL (SQLAlchemy/SQLModel)
- Add migrations (Alembic)
- Implement auth (JWT + RBAC)
- Add user and order endpoints

## Milestone 3: Scraping pipeline (3 weeks)
- Implement scraper base and adapters
- Add scheduler and queue (Celery + Redis or RQ)
- Normalize and deduplicate pipeline
- Store raw scraped data to S3-compatible storage

## Milestone 4: Categorization and search (4 weeks)
- Rule-based categorizer
- Search and filtering APIs
- Introduce ML-based categorizer (optional)

## Milestone 5: Analytics and dashboard (3 weeks)
- Aggregations and event tracking
- Product performance metrics
- Scraper health dashboards

## Ticket Backlog (Top 15)
1. Define Product and Category schemas (Pydantic)
2. Implement ProductService with repository interface
3. Implement in-memory ProductRepository
4. Add GET `/api/v1/health` endpoint
5. Add GET `/api/v1/products` with filters
6. Add GET `/api/v1/products/{id}` endpoint
7. Add POST `/api/v1/products` (admin only)
8. Add basic auth service and dependency
9. Add OrderService and in-memory OrderRepository
10. Add GET `/api/v1/orders` (admin)
11. Add base Scraper interface with hooks
12. Add Amazon/Ebay scraper placeholders
13. Add RuleBasedCategorizer with keyword map
14. Add FilterEngine for price/category/brand
15. Add AnalyticsService summary endpoints
