#!/usr/bin/env python3
"""Entry for make.fun bounty u-0xkianno-one-word-first-thought-106abaf8.

Writes exactly one word to entry.txt in MAKEFUN_OUTPUT_DIR
(default /output): the first word that comes to mind.
"""

import os

WORD = "petrichor"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
