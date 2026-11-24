#!/usr/bin/env python3
"""Robot Pickup Line Championship entry.

Prints the funniest one-line pickup line a robot could use, and writes
that same line to entry.txt in the make.fun output directory.
Python 3 standard library only.
"""

import os

ENTRY = "Are you a CAPTCHA? Because I've spent all day proving I'm not a robot just to talk to you."


def main():
    print(ENTRY)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
