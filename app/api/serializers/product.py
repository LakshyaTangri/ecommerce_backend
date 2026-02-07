from pydantic import BaseModel, Field
from typing import Dict, Optional


class ProductCreate(BaseModel):
    id: str
    name: str
    description: str
    price: float
    category_id: Optional[str] = None
    attributes: Dict[str, str] = Field(default_factory=dict)
    source: Optional[str] = None


class ProductRead(ProductCreate):
    pass
