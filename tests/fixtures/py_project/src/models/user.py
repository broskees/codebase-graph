from dataclasses import dataclass
from typing import Optional


@dataclass
class BaseModel:
    """Base model with common fields."""

    id: str
    created_at: str


@dataclass
class User(BaseModel):
    """A user in the system."""

    name: str
    email: str
    role: str = "user"


@dataclass
class AdminUser(User):
    """An admin user with extra permissions."""

    permissions: list[str] = None

    def __post_init__(self):
        if self.permissions is None:
            self.permissions = []
