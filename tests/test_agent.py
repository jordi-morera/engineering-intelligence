"""Tests for the EngineeringAgent foundation (no real API calls)."""

import pytest

from src.agent import EngineeringAgent
from src.config import Config


class FakeLLM:
    """A stub LLM client that returns a fixed response."""

    def __init__(self, response: str = "fixed response") -> None:
        self._response = response
        self.last_system = None
        self.last_user = None

    def chat(self, system_prompt: str, user_message: str) -> str:
        self.last_system = system_prompt
        self.last_user = user_message
        return self._response


@pytest.fixture
def config():
    return Config(openai_api_key="test-key", openai_model="gpt-4o")


def _load_system_prompt() -> str:
    # Load the canonical system prompt for a realistic test.
    from src.agent import SYSTEM_PROMPT_PATH
    return SYSTEM_PROMPT_PATH.read_text(encoding="utf-8").strip()


def test_agent_uses_system_prompt_and_user_input(config):
    llm = FakeLLM(response="hello")
    agent = EngineeringAgent(config=config, llm=llm, system_prompt="SYSTEM")
    result = agent.answer("What is a requirement?")
    assert result == "hello"
    assert llm.last_system == "SYSTEM"
    assert llm.last_user == "What is a requirement?"


def test_agent_defaults_system_prompt(config):
    llm = FakeLLM()
    agent = EngineeringAgent(config=config, llm=llm)
    assert "engineering intelligence" in agent._system_prompt.lower()


def test_agent_rejects_empty_input(config):
    llm = FakeLLM()
    agent = EngineeringAgent(config=config, llm=llm)
    with pytest.raises(ValueError):
        agent.answer("   ")


def test_system_prompt_file_exists():
    from src.agent import SYSTEM_PROMPT_PATH
    assert SYSTEM_PROMPT_PATH.exists()
    content = SYSTEM_PROMPT_PATH.read_text(encoding="utf-8")
    assert len(content) > 0
