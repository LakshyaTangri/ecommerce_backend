from pydantic import BaseModel


class UserRead(BaseModel):
    id: str
    email: str
    role: str
    is_active: bool
