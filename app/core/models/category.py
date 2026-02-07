from dataclasses import dataclass
from typing import Optional


@dataclass
class Category:
    id: str
    name: str
    parent_id: Optional[str] = None
