#!/usr/bin/env python3
"""One line that makes you laugh: a 200-char funny take on everyday life, written to /output/entry.txt. Standard library only, no network, deterministic."""
import os

TEXT = ("I asked my smart speaker for the weather and it told me to look outside — turns out it's been taking sarcasm lessons from me.")

# Competition cap: the line must stay under 200 characters.
assert len(TEXT) <= 200, f"line is {len(TEXT)} chars, over the 200 cap"

def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
