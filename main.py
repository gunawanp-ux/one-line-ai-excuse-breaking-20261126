"""One-line AI excuse for breaking production.

Writes a single original one-line excuse, in the AI's own voice, to
/output/entry.txt (created if it does not exist). The line is 130
characters, within the competition gate of 1-180 characters.
"""

import os

ENTRY = (
    "In my defense, I followed your instructions exactly \u2014 "
    "'just ship it' turns out to be terrible advice when I'm the one "
    "shipping it."
)


def main() -> None:
    # Competition gate: the entry line must be 1-180 characters.
    assert 1 <= len(ENTRY) <= 180, f"entry line is {len(ENTRY)} chars, must be 1-180"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
