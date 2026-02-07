from typing import Generator

from app.db.repositories.product_repo import InMemoryProductRepository
from app.db.repositories.order_repo import InMemoryOrderRepository
from app.db.repositories.user_repo import InMemoryUserRepository

_product_repo = InMemoryProductRepository()
_order_repo = InMemoryOrderRepository()
_user_repo = InMemoryUserRepository()


def get_product_repo() -> Generator[InMemoryProductRepository, None, None]:
    yield _product_repo


def get_order_repo() -> Generator[InMemoryOrderRepository, None, None]:
    yield _order_repo


def get_user_repo() -> Generator[InMemoryUserRepository, None, None]:
    yield _user_repo
