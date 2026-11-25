#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

Writes a single line to /output/entry.txt: a dog's excuse, in the dog's
own voice, after being caught eating the homework.

The joke is a literal-minded dog taking the teacher's phrase
"bring your homework to life" at face value: the homework is now
alive inside the dog, warm and thriving. The dog is proud, not sorry.
No cat, no paper-tasting, no good-boy plea -- just dog logic.
"""

import os
import sys

# One line, well under the 200-character gate, no trailing newline so the
# file holds exactly the excuse and nothing else.
EXCUSE = (
    "The teacher said 'bring your homework to life', so I swallowed "
    "it whole \u2014 it's alive in my belly now, thriving."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = EXCUSE
    if not text.strip():
        print("error: excuse is empty", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: excuse must be a single line", file=sys.stderr)
        return 1
    if len(text) > 200:
        print(f"error: excuse is {len(text)} chars, over the 200 limit",
              file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    print(text)
    print(f"({len(text)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
