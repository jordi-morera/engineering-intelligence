"""LLM Client — thin wrapper around the OpenAI API.

Separates raw model interaction from higher-level agent logic.
This layer should remain thin: it owns the API call and the response.
"""

import logging

from openai import OpenAI

from src.config import Config

logger = logging.getLogger(__name__)


class LLMClient:
    """Minimal client for OpenAI-compatible chat completions."""

    def __init__(self, config: Config) -> None:
        self._config = config
        self._client = OpenAI(api_key=config.openai_api_key)

    def chat(
        self,
        system_prompt: str,
        user_message: str,
        *,
        temperature: float = 0.2,
    ) -> str:
        """Send a chat completion request and return the assistant's reply.

        Args:
            system_prompt: The system-level instructions.
            user_message: The user's input.
            temperature: Sampling temperature (default 0.2 for determinism).

        Returns:
            The assistant's response text.

        Raises:
            RuntimeError: if the API call fails.
        """
        logger.info(
            "LLM request — model=%s temperature=%.1f prompt_len=%d user_len=%d",
            self._config.openai_model,
            temperature,
            len(system_prompt),
            len(user_message),
        )

        try:
            response = self._client.chat.completions.create(
                model=self._config.openai_model,
                temperature=temperature,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message},
                ],
            )
            content = response.choices[0].message.content or ""
            logger.info("LLM response — tokens_used=%s", response.usage)
            return content.strip()

        except Exception as exc:
            logger.error("LLM API call failed: %s", exc)
            raise RuntimeError(f"LLM API call failed: {exc}") from exc
