#!/usr/bin/env python3
"""The One-Line Laugh — writes one original funny line to /output/entry.txt.

The line is invented fresh in this session: no quotes, no copies, no
network, no input files. Pure Python stdlib, fully deterministic.
"""

import os

JOKE = "I finally learned to meditate, and now I ignore my problems with perfect posture."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate only accepts 1-200 characters of real text: enforce it here
    # so a bad line fails loudly instead of silently submitting junk.
    stripped = JOKE.strip()
    assert 1 <= len(stripped) <= 200, "joke must be 1-200 characters"
    assert stripped.count(".") == 1, "joke must be exactly one sentence"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(JOKE + "\n")


if __name__ == "__main__":
    main()
