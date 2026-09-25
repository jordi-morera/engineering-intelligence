"""EngineeringAgent — the top-level agent abstraction for Engineering Intelligence.

Conceptual flow:

    User Input
        ↓
    EngineeringAgent
        ↓
    LLM Client
        ↓
    Model API
        ↓
    Response

This is intentionally the simplest possible foundation. Tools, research,
reasoning loops and multi-agent behavior are deliberately not implemented yet.
"""

import logging
from pathlib import Path

from src.config import Config
from src.llm_client import LLMClient

logger = logging.getLogger(__name__)

SYSTEM_PROMPT_PATH = Path(__file__).resolve().parent.parent / "prompts" / "system.md"


class EngineeringAgent:
    """Answers engineering questions by composing a system prompt and user input.

    Args:
        config: Application configuration (API key, model, ...).
        llm: An LLMClient instance. Injectable for testing.
        system_prompt: The system instructions to use. Defaults to the canonical
            ``prompts/system.md``.
    """

    def __init__(
        self,
        config: Config,
        llm: LLMClient | None = None,
        system_prompt: str | None = None,
    ) -> None:
        self._config = config
        self._llm = llm if llm is not None else LLMClient(config)
        self._system_prompt = system_prompt if system_prompt is not None else self._load_system_prompt()

    @staticmethod
    def _load_system_prompt() -> str:
        if not SYSTEM_PROMPT_PATH.exists():
            raise FileNotFoundError(
                f"System prompt not found at {SYSTEM_PROMPT_PATH}"
            )
        return SYSTEM_PROMPT_PATH.read_text(encoding="utf-8")

    def answer(self, user_input: str) -> str:
        """Send a user question to the model and return the response.

        Args:
            user_input: The engineering question or context.

        Returns:
            The model's response as a string.

        Raises:
            ValueError: if user_input is empty.
            RuntimeError: if the underlying LLM call fails.
        """
        if not user_input or not user_input.strip():
            raise ValueError("user_input must not be empty")
        logger.info("EngineeringAgent answering: %.120s", user_input.strip())
        return self._llm.chat(self._system_prompt, user_input)
