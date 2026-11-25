"""The Tired Dark Lord: a 100-word villain monologue.

Reads the monologue from entry.txt (the single source of truth, shipped
in this repository) and writes it verbatim to /output/entry.txt.
Deterministic: the same input always produces the same output bytes.
"""

import os
import sys


def main() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), encoding="utf-8") as f:
        text = f.read()
    # Gate: the scorer only accepts UTF-8 text of 1 to 600 characters,
    # not only white space. Fail loudly instead of writing an invalid entry.
    if not text.strip():
        sys.exit("entry.txt is empty or only white space")
    if not 1 <= len(text) <= 600:
        sys.exit(f"entry.txt is {len(text)} characters, outside the 1-600 gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
