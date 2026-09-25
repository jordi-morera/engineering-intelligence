"""Tests for workflow loading."""

from pathlib import Path

import yaml

WORKFLOWS_DIR = Path(__file__).resolve().parent.parent / "workflows"


def _load_workflow(filename: str) -> dict:
    with open(WORKFLOWS_DIR / filename, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def test_requirement_workflow_loads():
    data = _load_workflow("requirement.yaml")
    assert data["type"] == "requirement"
    steps = [s["id"] for s in data["steps"]]
    assert "analyze_ticket" in steps
    assert "create_spec" in steps
    assert "critique_spec" in steps
    assert "validate_spec" in steps
    # required order of key steps
    assert steps.index("analyze_ticket") < steps.index("create_spec")
    assert steps.index("critique_spec") < steps.index("validate_spec")


def test_bug_workflow_loads():
    data = _load_workflow("bug.yaml")
    assert data["type"] == "bug"
    steps = [s["id"] for s in data["steps"]]
    assert "investigate_bug" in steps
    assert "identify_root_cause" in steps
    assert "propose_solution" in steps
    assert "create_spec" in steps
    assert "validate_spec" in steps
    # root cause must precede creating the spec
    assert steps.index("identify_root_cause") < steps.index("create_spec")


def test_workflows_have_guardrails():
    for filename in ("requirement.yaml", "bug.yaml"):
        data = _load_workflow(filename)
        assert "guardrails" in data
        assert len(data["guardrails"]) > 0
