from typing import Generator

from app.api.dependencies.db import get_user_repo
from app.core.models import User


def get_current_user() -> Generator[User, None, None]:
    user_repo_gen = get_user_repo()
    user_repo = next(user_repo_gen)
    yield user_repo.get_by_email("admin@example.com")
