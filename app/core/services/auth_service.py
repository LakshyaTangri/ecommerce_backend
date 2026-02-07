from typing import Optional

from app.core.interfaces.repositories import UserRepository
from app.core.interfaces.services import AuthServiceInterface
from app.core.models import User


class AuthService(AuthServiceInterface):
    def __init__(self, repo: UserRepository) -> None:
        self._repo = repo

    def authenticate(self, email: str, password: str) -> Optional[User]:
        user = self._repo.get_by_email(email)
        if user and user.is_active:
            return user
        return None
