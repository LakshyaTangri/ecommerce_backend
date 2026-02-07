from abc import ABC, abstractmethod
from typing import List, Optional

from app.core.models import Product, Order, User


class ProductServiceInterface(ABC):
    @abstractmethod
    def list_products(self, criteria: dict) -> List[Product]:
        raise NotImplementedError

    @abstractmethod
    def get_product(self, product_id: str) -> Optional[Product]:
        raise NotImplementedError

    @abstractmethod
    def create_product(self, product: Product) -> Product:
        raise NotImplementedError


class OrderServiceInterface(ABC):
    @abstractmethod
    def list_orders(self) -> List[Order]:
        raise NotImplementedError

    @abstractmethod
    def create_order(self, order: Order) -> Order:
        raise NotImplementedError


class AuthServiceInterface(ABC):
    @abstractmethod
    def authenticate(self, email: str, password: str) -> Optional[User]:
        raise NotImplementedError
