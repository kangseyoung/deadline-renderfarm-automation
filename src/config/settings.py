"""Public-safe configuration placeholders for the portfolio snapshot."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    deadline_command_path: str = os.getenv(
        "DEADLINE_COMMAND_PATH",
        "/path/to/deadlinecommand",
    )
    mongodb_uri: str = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
    database_name: str = os.getenv("DATABASE_NAME", "renderfarm")
    nas_root: str = os.getenv("NAS_ROOT", "/path/to/nas")
    app_env: str = os.getenv("APP_ENV", "development")


def load_settings() -> Settings:
    return Settings()
