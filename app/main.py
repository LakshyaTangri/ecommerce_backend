from fastapi import FastAPI

from app.config import settings
from app.logging import configure_logging
from app.api.routes.health import router as health_router
from app.api.routes.products import router as products_router
from app.api.routes.orders import router as orders_router
from app.api.routes.auth import router as auth_router


def create_app() -> FastAPI:
    configure_logging()
    app = FastAPI(title=settings.app_name)
    app.include_router(health_router, prefix=settings.api_prefix, tags=["health"])
    app.include_router(products_router, prefix=settings.api_prefix, tags=["products"])
    app.include_router(orders_router, prefix=settings.api_prefix, tags=["orders"])
    app.include_router(auth_router, prefix=settings.api_prefix, tags=["auth"])
    return app


app = create_app()
