from src.models.user import User, AdminUser


class AuthService:
    """Authentication service."""

    def __init__(self):
        self._users: dict[str, User] = {}

    def register(self, user: User) -> None:
        self._users[user.id] = user

    def get_user(self, user_id: str) -> User | None:
        return self._users.get(user_id)

    def is_admin(self, user: User) -> bool:
        return isinstance(user, AdminUser)


def create_token(user: User) -> str:
    """Create a session token for a user."""
    return f"token_{user.id}"
