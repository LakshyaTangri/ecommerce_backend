from typing import Dict

from app.core.interfaces.repositories import UserRepository
from app.core.models import User


class InMemoryUserRepository(UserRepository):
    def __init__(self) -> None:
        self._items: Dict[str, User] = {
            "admin@example.com": User(id="1", email="admin@example.com", role="admin", is_active=True)
        }

    def get_by_email(self, email: str) -> User | None:
        return self._items.get(email)
