"""Tests for configuration and environment validation."""

import pytest

from src.config import Config


def test_config_from_env_with_key(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setenv("OPENAI_MODEL", "gpt-4o-mini")
    config = Config.from_env()
    assert config.openai_api_key == "test-key"
    assert config.openai_model == "gpt-4o-mini"


def test_config_default_model(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.delenv("OPENAI_MODEL", raising=False)
    config = Config.from_env()
    assert config.openai_model == "gpt-4o"


def test_config_missing_key_exits(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    with pytest.raises(SystemExit) as exc_info:
        Config.from_env()
    assert exc_info.value.code == 1
