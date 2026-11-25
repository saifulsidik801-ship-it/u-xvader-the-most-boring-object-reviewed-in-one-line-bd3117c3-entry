#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line -- make.fun entry.

Writes a single one-line review of the most boring everyday object
imaginable -- the doorstop -- to /output/entry.txt. The joke comes from
how the object really behaves: a doorstop does its job so well you
forget it is there, right up until you meet it with your bare foot
in the dark.
"""

import os

ENTRY = "The doorstop does its job so perfectly you forget it exists \u2014 until 2 a.m., when it introduces itself to your bare foot."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
