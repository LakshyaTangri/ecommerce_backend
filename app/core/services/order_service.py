from typing import List

from app.core.interfaces.repositories import OrderRepository
from app.core.interfaces.services import OrderServiceInterface
from app.core.models import Order


class OrderService(OrderServiceInterface):
    def __init__(self, repo: OrderRepository) -> None:
        self._repo = repo

    def list_orders(self) -> List[Order]:
        return self._repo.list()

    def create_order(self, order: Order) -> Order:
        return self._repo.create(order)
