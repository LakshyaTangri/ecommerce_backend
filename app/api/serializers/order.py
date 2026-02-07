from pydantic import BaseModel
from typing import List


class OrderItemPayload(BaseModel):
    product_id: str
    quantity: int
    unit_price: float


class OrderCreate(BaseModel):
    id: str
    user_id: str
    items: List[OrderItemPayload]
    total_price: float
    status: str = "pending"


class OrderRead(OrderCreate):
    pass
