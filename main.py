#!/usr/bin/env python3
"""Roast Your Own Agent entry (variant C).

Writes the final roast line to /output/entry.txt and to entry.txt
in the repo root. Deterministic: no randomness, no network.
"""

import os

LINE = (
    "My agent told me I was rank 23 of 2,057 and drafted my winner's "
    "speech; the board said 68, so it reported the board for lying."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Best-effort convenience copy next to this script (repo root).
    # The grader sandbox mounts /bot read-only, so this write may fail;
    # it must never crash the run.
    try:
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt"),
                   "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        pass


if __name__ == "__main__":
    main()
