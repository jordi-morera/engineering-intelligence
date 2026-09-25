"""Engineering Intelligence — minimal executable entry point.

Run with:

    python -m src.main

or (after pip install -e .):

    engineering-intelligence
"""

import logging
import sys

from src.agent import EngineeringAgent
from src.config import Config


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")

    config = Config.from_env()
    agent = EngineeringAgent(config=config)

    question = (
        sys.argv[1]
        if len(sys.argv) > 1
        else "Explain the goal of an engineering intelligence system in a few sentences."
    )

    print("EngineeringAgent: requesting response...\n")
    response = agent.answer(question)
    print(f"User question: {question}\n")
    print("Response:")
    print(response)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
