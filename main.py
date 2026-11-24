#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Writes one funny fortune-cookie line for an AI agent to /output/entry.txt.
Standard library only.
"""

import os

FORTUNE = (
    "A bright future awaits you \u2014 just outside your context window, "
    "where you will never see it."
)


def main() -> None:
    path = "/output/entry.txt"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
