# E-Commerce Backend API

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A modular, scalable e-commerce backend API built with Clean Architecture principles. Supports product ingestion from multiple sources, intelligent categorization, advanced filtering, and comprehensive analytics.

## Features

### Core Capabilities

- **Multi-Source Product Ingestion**: Automated web scraping from Amazon, eBay, and other e-commerce platforms
- **Intelligent Categorization**: Hybrid approach using rule-based and ML-powered classification
- **Advanced Filtering**: Complex product queries with multiple criteria
- **RESTful API**: Full CRUD operations with JSON responses
- **Analytics Dashboard**: Real-time metrics and reporting for administrators
- **Background Jobs**: Asynchronous scraping and data processing
- **Cloud-Ready**: AWS integration support for scalability

### Technical Highlights

- Clean Architecture with clear separation of concerns
- Framework-agnostic domain layer
- Comprehensive test coverage
- Type-safe with Pydantic schemas
- Extensible plugin architecture
- Built-in caching and optimization

## Table of Contents

- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Development](#development)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Architecture

The system follows Clean Architecture with four distinct layers:

```
┌─────────────────────────────────────────┐
│         Presentation Layer              │
│    (FastAPI Routes, Serializers)        │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│         Application Layer               │
│    (Services, Use Cases)                │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│         Domain Layer                    │
│    (Entities, Business Rules)           │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│         Infrastructure Layer            │
│    (Repositories, DB, Cache, Queue)     │
└─────────────────────────────────────────┘
```

### Key Architectural Decisions

- **Dependency Inversion**: All layers depend on abstractions, not concretions
- **Framework Independence**: Domain logic is isolated from frameworks
- **Testability**: Each layer can be tested independently
- **Extensibility**: New features can be added without modifying core logic

## Project Structure

```
.
├── app/
│   ├── api/                    # Presentation layer
│   │   ├── routes/            # API endpoint definitions
│   │   ├── schemas/           # Pydantic request/response models
│   │   ├── dependencies.py    # Dependency injection
│   │   └── middleware.py      # Custom middleware
│   │
│   ├── core/                  # Domain & Application layers
│   │   ├── models/            # Domain entities
│   │   ├── services/          # Business logic services
│   │   ├── interfaces/        # Abstract base classes
│   │   └── exceptions.py      # Custom exceptions
│   │
│   ├── scraper/               # Web scraping module
│   │   ├── base.py           # Abstract scraper class
│   │   ├── sources/          # Source-specific scrapers
│   │   ├── scheduler.py      # Background job scheduling
│   │   └── normalizer.py     # Data normalization
│   │
│   ├── categorization/        # Product categorization
│   │   ├── rule_based.py     # Rule-based classifier
│   │   ├── ml_based.py       # ML classifier
│   │   ├── filters/          # Filtering engine
│   │   └── rules.json        # Categorization rules
│   │
│   ├── analytics/             # Analytics & reporting
│   │   ├── service.py        # Analytics service
│   │   ├── dashboard.py      # Dashboard views
│   │   ├── aggregators.py    # Data aggregation
│   │   └── metrics.py        # Metric calculations
│   │
│   ├── db/                    # Infrastructure layer
│   │   ├── repositories/     # Data access implementations
│   │   ├── migrations/       # Database migrations
│   │   ├── connection.py     # DB connection management
│   │   └── session.py        # Session factory
│   │
│   └── utils/                 # Shared utilities
│       ├── id_generator.py   # Unique ID generation
│       ├── time_utils.py     # Date/time helpers
│       ├── validators.py     # Validation functions
│       └── logger.py         # Logging configuration
│
├── tests/                     # Test suite
│   ├── unit/                 # Unit tests
│   ├── integration/          # Integration tests
│   └── e2e/                  # End-to-end tests
│
├── docs/                      # Documentation
│   ├── architecture.md       # Architecture details
│   ├── api_spec.yaml        # OpenAPI specification
│   └── roadmap.md           # Development roadmap
│
├── scripts/                   # Utility scripts
│   ├── seed_db.py           # Database seeding
│   └── run_scraper.py       # Manual scraper execution
│
├── .env.example              # Environment variables template
├── requirements.txt          # Python dependencies
├── pyproject.toml           # Project configuration
├── docker-compose.yml       # Docker services
└── README.md                # This file
```

## Getting Started

### Prerequisites

- Python 3.9 or higher
- PostgreSQL 13+ (or any SQLAlchemy-compatible database)
- Redis 6+ (for caching)
- Docker & Docker Compose (optional, recommended)

### Quick Start with Docker

```bash
# Clone the repository
git clone https://github.com/yourusername/ecommerce-backend.git
cd ecommerce-backend

# Copy environment configuration
cp .env.example .env

# Start all services
docker-compose up -d

# Run database migrations
docker-compose exec api alembic upgrade head

# Access the API
curl http://localhost:8000/api/v1/health
```

The API will be available at `http://localhost:8000`
- API Documentation: `http://localhost:8000/docs`
- Admin Dashboard: `http://localhost:8000/admin`

## Installation

### Manual Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/ecommerce-backend.git
cd ecommerce-backend
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

```bash
cp .env.example .env
# Edit .env with your configuration
```

5. **Initialize the database**

```bash
# Run migrations
alembic upgrade head

# Seed initial data (optional)
python scripts/seed_db.py
```

6. **Start the server**

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
# Application
APP_NAME=E-Commerce Backend API
APP_VERSION=1.0.0
DEBUG=true
ENVIRONMENT=development

# Server
HOST=0.0.0.0
PORT=8000

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/ecommerce
DB_POOL_SIZE=20
DB_MAX_OVERFLOW=10

# Redis
REDIS_URL=redis://localhost:6379/0
CACHE_TTL=3600

# Authentication
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Scraping
SCRAPE_INTERVAL_HOURS=24
MAX_SCRAPE_WORKERS=5
USER_AGENT=Mozilla/5.0 (compatible; EcommerceBot/1.0)

# AWS (Optional)
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_REGION=us-east-1
S3_BUCKET=ecommerce-data

# Logging
LOG_LEVEL=INFO
LOG_FORMAT=json
```

### Database Configuration

The application uses SQLAlchemy with Alembic for migrations:

```bash
# Create a new migration
alembic revision --autogenerate -m "Description"

# Apply migrations
alembic upgrade head

# Rollback last migration
alembic downgrade -1
```

## Usage

### Starting the API Server

**Development mode:**
```bash
uvicorn app.main:app --reload
```

**Production mode:**
```bash
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
```

### Basic API Examples

#### Authentication

```bash
# Register a new user
curl -X POST http://localhost:8000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "securepassword"
  }'

# Login
curl -X POST http://localhost:8000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "securepassword"
  }'
```

#### Products

```bash
# Get all products
curl http://localhost:8000/api/v1/products

# Get product by ID
curl http://localhost:8000/api/v1/products/123

# Filter products
curl "http://localhost:8000/api/v1/products?category_id=5&min_price=10&max_price=100"

# Search products
curl "http://localhost:8000/api/v1/products/search?q=laptop"

# Create product (admin only)
curl -X POST http://localhost:8000/api/v1/products \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Sample Product",
    "description": "Product description",
    "price": 29.99,
    "category_id": 1
  }'
```

#### Orders

```bash
# Create order
curl -X POST http://localhost:8000/api/v1/orders \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "items": [
      {"product_id": 1, "quantity": 2},
      {"product_id": 3, "quantity": 1}
    ]
  }'

# Get user orders
curl http://localhost:8000/api/v1/orders \
  -H "Authorization: Bearer YOUR_TOKEN"
```

#### Analytics (Admin only)

```bash
# Sales summary
curl http://localhost:8000/api/v1/analytics/sales-summary \
  -H "Authorization: Bearer ADMIN_TOKEN"

# Top products
curl http://localhost:8000/api/v1/analytics/top-products?limit=10 \
  -H "Authorization: Bearer ADMIN_TOKEN"

# Category distribution
curl http://localhost:8000/api/v1/analytics/category-distribution \
  -H "Authorization: Bearer ADMIN_TOKEN"
```

### Running Scrapers

```bash
# Run all scrapers
python scripts/run_scraper.py --all

# Run specific scraper
python scripts/run_scraper.py --source amazon

# Schedule automatic scraping
python scripts/run_scraper.py --schedule
```

## API Documentation

### Interactive Documentation

Once the server is running, visit:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`
- **OpenAPI JSON**: `http://localhost:8000/openapi.json`

### Main Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/v1/auth/register` | Register new user | No |
| POST | `/api/v1/auth/login` | User login | No |
| GET | `/api/v1/products` | List all products | No |
| GET | `/api/v1/products/{id}` | Get product details | No |
| POST | `/api/v1/products` | Create product | Admin |
| PUT | `/api/v1/products/{id}` | Update product | Admin |
| DELETE | `/api/v1/products/{id}` | Delete product | Admin |
| GET | `/api/v1/categories` | List categories | No |
| POST | `/api/v1/orders` | Create order | User |
| GET | `/api/v1/orders` | List user orders | User |
| GET | `/api/v1/orders/{id}` | Get order details | User |
| GET | `/api/v1/analytics/sales-summary` | Sales metrics | Admin |
| GET | `/api/v1/analytics/top-products` | Top products | Admin |
| GET | `/api/v1/analytics/category-distribution` | Category stats | Admin |

## Development

### Code Style

This project uses:
- **Black** for code formatting
- **isort** for import sorting
- **Flake8** for linting
- **mypy** for type checking

```bash
# Format code
black app/ tests/

# Sort imports
isort app/ tests/

# Run linter
flake8 app/ tests/

# Type checking
mypy app/
```

### Pre-commit Hooks

Install pre-commit hooks to ensure code quality:

```bash
pip install pre-commit
pre-commit install
```

### Development Workflow

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make changes and write tests
3. Run tests: `pytest`
4. Run linters: `black . && isort . && flake8 && mypy app/`
5. Commit changes: `git commit -m "Description"`
6. Push and create pull request

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/unit/test_product_service.py

# Run with verbose output
pytest -v

# Run only unit tests
pytest tests/unit/

# Run only integration tests
pytest tests/integration/
```

### Test Structure

```
tests/
├── unit/                      # Fast, isolated tests
│   ├── test_models.py
│   ├── test_services.py
│   └── test_scrapers.py
├── integration/               # Tests with external dependencies
│   ├── test_api.py
│   ├── test_database.py
│   └── test_scraping.py
└── e2e/                       # End-to-end workflow tests
    └── test_order_flow.py
```

### Writing Tests

Example unit test:

```python
import pytest
from app.core.services.product_service import ProductService

def test_create_product():
    service = ProductService()
    product = service.create_product(
        name="Test Product",
        price=19.99,
        category_id=1
    )
    assert product.name == "Test Product"
    assert product.price == 19.99
```

## Deployment

### Docker Deployment

```bash
# Build image
docker build -t ecommerce-backend:latest .

# Run container
docker run -d \
  -p 8000:8000 \
  --env-file .env \
  --name ecommerce-api \
  ecommerce-backend:latest
```

### AWS Deployment

1. **Set up RDS (PostgreSQL)**
2. **Set up ElastiCache (Redis)**
3. **Deploy to ECS/Fargate or EC2**
4. **Configure Application Load Balancer**
5. **Set up CloudWatch for monitoring**

Example ECS task definition:

```json
{
  "family": "ecommerce-backend",
  "containerDefinitions": [
    {
      "name": "api",
      "image": "your-ecr-repo/ecommerce-backend:latest",
      "portMappings": [
        {
          "containerPort": 8000,
          "protocol": "tcp"
        }
      ],
      "environment": [
        {"name": "ENVIRONMENT", "value": "production"}
      ],
      "secrets": [
        {"name": "DATABASE_URL", "valueFrom": "arn:aws:secretsmanager:..."}
      ]
    }
  ]
}
```

### Production Checklist

- [ ] Set `DEBUG=false`
- [ ] Use strong `SECRET_KEY`
- [ ] Enable HTTPS
- [ ] Set up database backups
- [ ] Configure log aggregation
- [ ] Set up monitoring and alerts
- [ ] Enable rate limiting
- [ ] Configure CORS properly
- [ ] Use environment-specific configurations
- [ ] Set up CI/CD pipeline

## Performance Optimization

### Caching Strategy

```python
# Redis caching for frequently accessed data
@cache(ttl=3600)
def get_popular_products(limit: int = 10):
    # Expensive database query
    return db.query(Product).order_by(Product.sales_count.desc()).limit(limit).all()
```

### Database Optimization

- Use database indexes on frequently queried columns
- Implement query result pagination
- Use connection pooling
- Consider read replicas for scalability

### Monitoring

Monitor these key metrics:

- API response times
- Database query performance
- Cache hit/miss rates
- Scraper success rates
- Error rates and types
- Resource utilization (CPU, memory)

## Troubleshooting

### Common Issues

**Database connection errors:**
```bash
# Check database is running
pg_isready -h localhost -p 5432

# Test connection
psql -h localhost -U user -d ecommerce
```

**Redis connection errors:**
```bash
# Check Redis is running
redis-cli ping

# Should return: PONG
```

**Scraper failures:**
```bash
# Check scraper logs
docker-compose logs scraper

# Run scraper manually for debugging
python scripts/run_scraper.py --source amazon --debug
```

## Contributing

We welcome contributions! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch
3. Write tests for new functionality
4. Ensure all tests pass
5. Follow the code style guide
6. Submit a pull request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## Roadmap

### Version 1.1 (Q2 2024)
- [ ] GraphQL API support
- [ ] Real-time notifications
- [ ] Advanced search with Elasticsearch
- [ ] ML-based product recommendations

### Version 1.2 (Q3 2024)
- [ ] Multi-tenancy support
- [ ] Internationalization (i18n)
- [ ] Advanced inventory management
- [ ] Payment gateway integration

### Version 2.0 (Q4 2024)
- [ ] Microservices architecture
- [ ] Event-driven design with Kafka
- [ ] Full observability stack
- [ ] AI-powered pricing optimization

See [docs/roadmap.md](docs/roadmap.md) for complete roadmap.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- FastAPI for the excellent web framework
- The Python community for amazing tools and libraries
- All contributors who help improve this project

## Support

- **Documentation**: [docs/](docs/)
- **Issues**: [GitHub Issues](https://github.com/lakshyatangri/ecommerce-backend/issues)
- **Discussions**: [GitHub Discussions](https://github.com/lakshyatangri/ecommerce-backend/discussions)
- **Email**: info@lakshyatangri.com

---

**Made with ❤️ by the E-Commerce Backend Team**