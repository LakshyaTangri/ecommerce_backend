from abc import ABC, abstractmethod
from typing import List, Optional

from app.core.models import Product, Order, User


class ProductRepository(ABC):
    @abstractmethod
    def list(self) -> List[Product]:
        raise NotImplementedError

    @abstractmethod
    def get(self, product_id: str) -> Optional[Product]:
        raise NotImplementedError

    @abstractmethod
    def create(self, product: Product) -> Product:
        raise NotImplementedError


class OrderRepository(ABC):
    @abstractmethod
    def list(self) -> List[Order]:
        raise NotImplementedError

    @abstractmethod
    def get(self, order_id: str) -> Optional[Order]:
        raise NotImplementedError

    @abstractmethod
    def create(self, order: Order) -> Order:
        raise NotImplementedError


class UserRepository(ABC):
    @abstractmethod
    def get_by_email(self, email: str) -> Optional[User]:
        raise NotImplementedError
