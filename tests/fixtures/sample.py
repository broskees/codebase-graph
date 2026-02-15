from dataclasses import dataclass
from typing import Optional


@dataclass
class Config:
    """Application configuration."""

    host: str = "localhost"
    port: int = 8080
    debug: bool = False


class AppServer:
    """A simple application server."""

    def __init__(self, config: Config) -> None:
        self.config = config
        self._running = False

    def start(self) -> None:
        """Start the server."""
        self._running = True

    def stop(self) -> None:
        """Stop the server."""
        self._running = False

    def is_running(self) -> bool:
        """Check if the server is running."""
        return self._running


def create_app(host: str = "localhost", port: int = 8080) -> AppServer:
    """Create and return a new AppServer instance."""
    config = Config(host=host, port=port)
    return AppServer(config)
