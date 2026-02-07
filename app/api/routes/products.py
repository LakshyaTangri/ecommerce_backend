from fastapi import APIRouter, Depends, HTTPException
from typing import Optional

from app.api.serializers.product import ProductCreate, ProductRead
from app.api.dependencies.db import get_product_repo
from app.core.services.product_service import ProductService
from app.categorization.filters.filter_engine import FilterEngine
from app.core.models import Product

router = APIRouter()


def _get_service(repo=Depends(get_product_repo)) -> ProductService:
    return ProductService(repo=repo, filter_engine=FilterEngine())


@router.get("/products", response_model=list[ProductRead])
def list_products(
    category: Optional[str] = None,
    price_min: Optional[float] = None,
    price_max: Optional[float] = None,
    brand: Optional[str] = None,
    service: ProductService = Depends(_get_service),
) -> list[ProductRead]:
    criteria = {
        "category": category,
        "price_min": price_min,
        "price_max": price_max,
        "brand": brand,
    }
    return service.list_products(criteria)


@router.get("/products/{product_id}", response_model=ProductRead)
def get_product(product_id: str, service: ProductService = Depends(_get_service)) -> ProductRead:
    product = service.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.post("/products", response_model=ProductRead)
def create_product(payload: ProductCreate, service: ProductService = Depends(_get_service)) -> ProductRead:
    product = Product(
        id=payload.id,
        name=payload.name,
        description=payload.description,
        price=payload.price,
        category_id=payload.category_id,
        attributes=payload.attributes,
        source=payload.source,
    )
    return service.create_product(product)
