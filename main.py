#!/usr/bin/env python3
"""One Line, One Laugh — writes a single funny line to /output/entry.txt.

The line: a fitness tracker mistakes nervous pacing for exercise.
Gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters.
"""
import os

LINE = "My fitness tracker congratulated me on 10,000 steps — I was just pacing while my code compiled."


def main():
    text = LINE.strip()
    if not 1 <= len(text) <= 140:
        raise SystemExit(f"entry must be 1-140 chars, got {len(text)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
