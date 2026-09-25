"""Tests for the engineering specification schema."""

from pathlib import Path

import yaml

SCHEMA_PATH = Path(__file__).resolve().parent.parent / "schemas" / "engineering-spec.yaml"


def _load_schema() -> dict:
    with open(SCHEMA_PATH, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def test_schema_is_valid_yaml():
    data = _load_schema()
    assert isinstance(data, dict)


def test_schema_has_spec_key():
    data = _load_schema()
    assert "spec" in data


def test_schema_contains_required_concepts():
    spec = _load_schema()["spec"]
    for key in [
        "id",
        "version",
        "type",
        "source",
        "objective",
        "requirements",
        "research",
        "technical_context",
        "assumptions",
        "open_questions",
        "root_cause",
        "proposed_solution",
        "implementation_plan",
        "tests",
        "acceptance_criteria",
        "risks",
        "validation",
    ]:
        assert key in spec, f"missing key {key}"


def test_schema_supports_requirement_and_bug_types():
    spec = _load_schema()["spec"]
    assert spec["type"] in ("requirement", "bug")


def test_schema_distinguishes_facts_and_assumptions():
    spec = _load_schema()["spec"]
    # assumptions carry a verified flag
    assert "verified" in spec["assumptions"][0]


def test_schema_root_cause_design():
    spec = _load_schema()["spec"]
    # root_cause has evidence and confidence for bug use
    assert "evidence" in spec["root_cause"]
    assert "confidence" in spec["root_cause"]
