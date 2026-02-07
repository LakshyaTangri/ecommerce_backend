from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Optional


@dataclass
class Product:
    id: str
    name: str
    description: str
    price: float
    category_id: Optional[str]
    attributes: Dict[str, str] = field(default_factory=dict)
    source: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
