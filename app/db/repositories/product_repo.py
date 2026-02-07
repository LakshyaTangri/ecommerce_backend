from typing import Dict, List

from app.core.interfaces.repositories import ProductRepository
from app.core.models import Product


class InMemoryProductRepository(ProductRepository):
    def __init__(self) -> None:
        self._items: Dict[str, Product] = {}

    def list(self) -> List[Product]:
        return list(self._items.values())

    def get(self, product_id: str) -> Product | None:
        return self._items.get(product_id)

    def create(self, product: Product) -> Product:
        self._items[product.id] = product
        return product
