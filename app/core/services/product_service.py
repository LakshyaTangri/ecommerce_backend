from typing import List, Optional

from app.core.interfaces.repositories import ProductRepository
from app.core.interfaces.services import ProductServiceInterface
from app.core.models import Product
from app.categorization.filters.filter_engine import FilterEngine


class ProductService(ProductServiceInterface):
    def __init__(self, repo: ProductRepository, filter_engine: FilterEngine) -> None:
        self._repo = repo
        self._filters = filter_engine

    def list_products(self, criteria: dict) -> List[Product]:
        products = self._repo.list()
        return self._filters.apply_filters(products, criteria)

    def get_product(self, product_id: str) -> Optional[Product]:
        return self._repo.get(product_id)

    def create_product(self, product: Product) -> Product:
        return self._repo.create(product)
