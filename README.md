<<<<<<< HEAD
# engineering-intelligence
Agent that converts tickets into validated specifications before deploying
=======
# Engineering Intelligence

An AI-powered engineering intelligence system designed to transform engineering work
items into **validated specifications before implementation**.

## Core philosophy

```
WHAT + WHY        (understanding, investigating, specifying)
     before
HOW + DO          (implementation)
```

Engineering Intelligence focuses entirely on the first half. Understanding must come
before doing.

## System boundaries

The project is conceptually divided into two systems:

### System 1 — Engineering Intelligence (WHAT + WHY)
Investigates and understands engineering work. It is capable of understanding Jira
tickets, researching documentation and repositories, identifying requirements and root
causes, producing evidence-backed specifications, critiquing and validating them, and
requiring human approval before implementation. **It never modifies source code.**

### System 2 — Engineering Execution (HOW + DO)
Consumes an approved specification and performs implementation, tests, static analysis,
self-review, pull request creation, and Jira updates. **Out of scope for now.**

## Current scope

This is an early foundation. The current implementation is a minimal, runnable
`EngineeringAgent` that composes a system prompt and a user message and calls an LLM.
It does **not** yet integrate with Jira, Confluence, or repositories. Those are future
capabilities; the architecture is designed so they can be added without rewriting the core.

## Project structure

```
src/            Core Python code (agent, LLM client, config, entry point)
skills/         Skill contracts (methodology for future capabilities)
prompts/        Prompt templates (e.g. system.md)
schemas/        Structured contracts (e.g. engineering-spec.yaml)
workflows/      Workflow definitions (requirement.yaml, bug.yaml)
specs/          Output location for produced specifications
evaluations/    Evaluation strategy and metrics
runs/           Execution run logs
tests/          Unit tests
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env   # then add your OPENAI_API_KEY
```

## Run

```bash
python -m src.main
```

Without an API key, the application prints a clear configuration error and exits.

## Run tests

```bash
pytest
```

## Future architecture

```
Jira
 ↓
Agent
 ↓
Research
 ├── Confluence
 └── Repository
 ↓
Evidence
 ↓
Specification
 ↓
Critic
 ↓
Validation
 ↓
Human Approval
 ↓
System 2
```

## Read-only by default

Engineering Intelligence is fundamentally an investigation/specification system.
External integrations should initially be read-only. The foundation contains no
mechanisms for modifying repositories, tickets, or branches.
>>>>>>> 5ba99c3 (Initial commit)
