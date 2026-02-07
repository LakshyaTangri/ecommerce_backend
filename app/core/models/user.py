from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    id: str
    email: str
    role: str
    is_active: bool = True
