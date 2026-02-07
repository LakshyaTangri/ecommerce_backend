from dataclasses import dataclass, field
from typing import List


@dataclass
class OrderItem:
    product_id: str
    quantity: int
    unit_price: float


@dataclass
class Order:
    id: str
    user_id: str
    items: List[OrderItem] = field(default_factory=list)
    total_price: float = 0.0
    status: str = "pending"
