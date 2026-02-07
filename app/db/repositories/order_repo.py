from typing import Dict, List

from app.core.interfaces.repositories import OrderRepository
from app.core.models import Order


class InMemoryOrderRepository(OrderRepository):
    def __init__(self) -> None:
        self._items: Dict[str, Order] = {}

    def list(self) -> List[Order]:
        return list(self._items.values())

    def get(self, order_id: str) -> Order | None:
        return self._items.get(order_id)

    def create(self, order: Order) -> Order:
        self._items[order.id] = order
        return order
