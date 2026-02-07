from fastapi import APIRouter, Depends

from app.api.serializers.order import OrderCreate, OrderRead
from app.api.dependencies.db import get_order_repo
from app.core.services.order_service import OrderService
from app.core.models import Order, OrderItem

router = APIRouter()


def _get_service(repo=Depends(get_order_repo)) -> OrderService:
    return OrderService(repo=repo)


@router.get("/orders", response_model=list[OrderRead])
def list_orders(service: OrderService = Depends(_get_service)) -> list[OrderRead]:
    return service.list_orders()


@router.post("/orders", response_model=OrderRead)
def create_order(payload: OrderCreate, service: OrderService = Depends(_get_service)) -> OrderRead:
    items = [OrderItem(**i.model_dump()) for i in payload.items]
    order = Order(id=payload.id, user_id=payload.user_id, items=items, total_price=payload.total_price, status=payload.status)
    return service.create_order(order)
