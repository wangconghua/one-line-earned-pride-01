#!/usr/bin/env python3
"""One Line of Earned Pride: a quiet, earned moment of pride in one line.

The line: a seventy-two-year-old woman reads a letter aloud, every word
her own - the first thing she has ever read that no one had read to her.
A long effort finally landing, in a concrete scene, with the pride
arriving at the last word.
"""

import os

ENTRY = "At seventy-two she read the letter aloud, slowly, every word her own \u2014 the first thing she had ever read that no one had read to her."

OUT_PATH = "/output/entry.txt"


def validate_entry(text):
    """Check the entry against the bounty gate before writing it.

    The gate requires UTF-8 text of 1 to 240 characters, not only
    whitespace, on a single line. We also refuse leading or trailing
    whitespace and control characters, so the file the judge reads is
    exactly the line as written - no hidden padding the judge would
    have to look past.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= 240:
        raise ValueError(f"entry must be 1-240 characters, got {len(text)}")
    if text.isspace():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry must not contain control characters")
    text.encode("utf-8")  # raises if the line is not valid UTF-8 text
    return text


def main():
    entry = validate_entry(ENTRY)
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
