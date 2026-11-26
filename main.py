#!/usr/bin/env python3
"""Rejected Olympic Sports entry: writes one funny one-line sport to /output/entry.txt.

The entry is a single line: a made-up Olympic event, plausible enough to
sound like a broadcast, absurd enough to be funny.
"""

import os

ENTRY = "Speed Napping: athletes race to fall asleep; snoring is a foul, drooling scores style points."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
