# Backend Documentation

## Requirement Description
- Build a modular e-commerce backend API that supports product ingestion (scraping), normalization, categorization, and exposure via REST/JSON.
- Provide filtering, search-ready data structures, and analytics endpoints for admins.
- Maintain clean, testable, and extensible architecture with clear separation of concerns.
- Support background jobs for scraping and aggregation.
- Be cloud-ready (AWS), with storage, messaging, and observability integrations.

## Architecture Description
The system follows Clean Architecture with four layers: Presentation (API), Application (services), Domain (models and interfaces), and Infrastructure (repositories, DB, cache, queues). Domain models are framework-agnostic; services orchestrate use cases; repositories abstract persistence; API routes compose services and dependencies.

## ABB Matrix (Architecture Building Blocks)
| ABB | Responsibility | Key Modules | Interfaces | Notes |
| --- | --- | --- | --- | --- |
| Presentation Layer | REST/JSON API and request/response validation | `app/api` | API routes, serializers | FastAPI routes, Pydantic schemas |
| Application Layer | Orchestrate use cases | `app/core/services` | Service interfaces | Business workflows |
| Domain Layer | Core entities and rules | `app/core/models` | Domain models | OOP models, dataclasses |
| Infrastructure Layer | Persistence, cache, queues | `app/db`, `app/utils` | Repository interfaces | Replace in-memory repos with DB |

## Components Description
Components are solution building blocks (SBBs) that encapsulate capabilities and are independently testable. Each component exposes interfaces to keep coupling low.

## SBB Matrix (Solution Building Blocks)
| SBB | Responsibility | Key Modules | Interfaces |
| --- | --- | --- | --- |
| API Gateway | Serve REST endpoints | `app/api/routes` | Route handlers |
| Auth Service | Login/authentication | `app/core/services/auth_service.py` | `AuthServiceInterface` |
| Product Service | Product CRUD and filters | `app/core/services/product_service.py` | `ProductServiceInterface` |
| Order Service | Order workflows | `app/core/services/order_service.py` | `OrderServiceInterface` |
| Scraping Service | Fetch and normalize products | `app/scraper` | `Scraper` base |
| Categorization Engine | Classify products | `app/categorization` | `RuleBasedCategorizer` |
| Filtering Engine | Apply filters to products | `app/categorization/filters` | `FilterEngine` |
| Analytics Engine | Aggregate metrics | `app/analytics` | `AnalyticsService` |
| Notification Service | Future extension | N/A | N/A |

## Root Structure & Modules Explained
- `app/api` REST endpoints, serializers, and dependencies.
- `app/core` domain models, service interfaces, and business logic.
- `app/scraper` scraping base classes, sources, and scheduler jobs.
- `app/categorization` rule-based and ML categorization plus filters.
- `app/analytics` analytics services and dashboard views.
- `app/db` repository implementations and migrations.
- `app/utils` utility helpers (IDs, time).
- `docs` architecture and roadmap documentation.

## Classes & Objects Defined
### Core Domain Models
- `User(id, email, role, is_active)`
- `Product(id, name, description, price, category_id, attributes, source, created_at)`
- `Category(id, name, parent_id)`
- `Order(id, user_id, items, total_price, status)`
- `OrderItem(product_id, quantity, unit_price)`

### Scraping Layer
- `Scraper.fetch()`
- `Scraper.parse(raw)`
- `Scraper.normalize(parsed)`
- `AmazonScraper(Scraper)`
- `EbayScraper(Scraper)`
- `ScrapeJob(source, status, last_run)`

### Categorization & Filtering
- `RuleBasedCategorizer.classify(product_name)`
- `MLBasedCategorizer.classify(product_name)`
- `FilterEngine.apply_filters(products, criteria)`

### Analytics & Dashboard
- `AnalyticsService.sales_summary()`
- `AnalyticsService.top_products()`
- `AnalyticsService.category_distribution()`
- `DashboardView.render_metrics()`
