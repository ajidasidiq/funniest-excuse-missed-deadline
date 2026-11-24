#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes one deadpan excuse, in the agent's own voice, to /output/entry.txt.
The excuse grows out of the agent's own machinery: it did submit the work,
to an endpoint that answered like a real one. The punchline is the last
word, and nothing is explained after it.
"""

import os

ENTRY = "I submitted the work on time. The endpoint accepted it, thanked me, and was a mock."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
