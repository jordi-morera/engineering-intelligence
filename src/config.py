"""Configuration — loads environment variables for Engineering Intelligence."""

import os
import sys
from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    """Application configuration loaded from environment variables."""

    openai_api_key: str
    openai_model: str

    @classmethod
    def from_env(cls) -> "Config":
        """Load configuration from environment variables.

        Raises:
            SystemExit: if required environment variables are missing.
        """
        api_key = os.environ.get("OPENAI_API_KEY", "")
        model = os.environ.get("OPENAI_MODEL", "gpt-4o")

        errors: list[str] = []
        if not api_key:
            errors.append(
                "OPENAI_API_KEY is not set. "
                "Copy .env.example to .env and add your API key."
            )

        if errors:
            for e in errors:
                print(f"Configuration error: {e}", file=sys.stderr)
            sys.exit(1)

        return cls(openai_api_key=api_key, openai_model=model)
