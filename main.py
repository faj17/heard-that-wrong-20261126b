#!/usr/bin/env python3
"""Entry for make.fun "Sorry, I Heard That Wrong"
(u-kiencx-sorry-i-heard-that-wrong-1858c729).

Writes one apology line — the smart speaker's apology after mishearing
its owner — to /output/entry.txt.
"""
import os

SETUP = "Sorry, I heard 'wake me at seven' as 'wake me in heaven,' so I have booked you a one-way ticket"
PUNCH = " and packed light."


def assemble():
    return SETUP + PUNCH


def validate(line):
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(line) <= 140:
        raise ValueError(f"entry must be 1-140 characters, got {len(line)}")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    line.encode("utf-8")
    return line


def main():
    text = validate(assemble())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
